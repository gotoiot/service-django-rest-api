import datetime

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, permissions, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.exceptions import APIException

from assesments.models import Assesment, Instance, Option, Question, Taker
from assesments.serializers import (AssesmentSerializer, InstanceSerializer,
                                    OptionSerializer, QuestionSerializer,
                                    TakerSerializer)


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is the main entry point for the Assesment app.
    From this endpoint you can explore each resources by clicking in each link below.
    """
    return Response({
        'assesments': reverse('assesments:assesment-list', request=request, format=format),
        'instances': reverse('assesments:instance-list', request=request, format=format),
        'takers': reverse('assesments:taker-list', request=request, format=format),
        'questions': reverse('assesments:question-list', request=request, format=format),
        'options': reverse('assesments:option-list', request=request, format=format),
    })


class AssesmentList(generics.ListAPIView):
    """
    From this endpoint you can get the list of assesments.
    """
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AssesmentDetail(generics.RetrieveAPIView):
    """
    From this endpoint you can get the details of assesments created.
    """
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AssesmentStatus(APIView):
    """
    From this endpoint you can get the assesment status based in its id.
    """
    def get(self, request, pk, format=None):
        _ = get_object_or_404(Assesment, pk=pk)
        return Response({"message": "success"}, status=status.HTTP_200_OK)


class InstanceList(generics.ListAPIView):
    """
    From this endpoint you can get the list of instances created.
    """
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InstanceDetail(generics.RetrieveAPIView):
    """
    From this endpoint you can get the details of instances created.
    """
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class InstanceCreate(APIView):
    """ 
    From this endpoint you can create and assesment instance based in assesment ID.

    Here is an example for creating a new instance by providing taker data:
        
    {
        "first_name": "Guido",
        "last_name": "Van Rossum",
        "email": "guido@python.org"
    }        
    
    Here are some possibilities which don't create new instances:
    - If user data is invalid a 400 status is returned.
    - If user has an active instance a 405 status is returned.
    - If taker has an inactive instance for an assesment, the instance ID is returned instead of creating a new one.
    """
    def post(self, request, pk, format=None):
        assesment = get_object_or_404(Assesment, pk=pk)
        taker_serializer = TakerSerializer(data=request.data)
        if not taker_serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        taker = taker_serializer.save()

        if taker.instance_set.filter(active=True).count() > 0:
            return Response({"message": "taker has active(s) test instance(s)"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if taker.instance_set.filter(active=False, assesment=assesment).count() > 0:
            instance = taker.instance_set.filter(active=False, assesment=assesment).first()
        else:
            instance = Instance(taker=taker, assesment=assesment, start_date=timezone.now(), end_date=timezone.now())
            instance.save()
        
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url'))
        return Response(instance_serializer.data, status=status.HTTP_201_CREATED)


class InstanceTest(APIView):
    """
    From this endpoint you can test if an instance is OK to be initiated.
    """
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url', 'active', 'finalized'))
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class InstanceStart(APIView):
    """
    From this endpoint you can start an instance, if the instance is not activated.
    If the instance is activated a 405 status is returned.
    """
    def post(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if instance.active:
            return Response({"message": "instance was already activated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to start a finished instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.start_time = timezone.now()
        instance.end_time = instance.start_time + datetime.timedelta(minutes=instance.duration)
        instance.active = True
        instance.save()
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url', 'active', 'duration', 'start_date', 'end_date'))
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class InstanceQuestionDetail(APIView):
    """
    From this endpoint you can get the question details for a selected question of an assesment instance.
    Here are some possible errors:
    - If the instance is inactive a 405 status is returned.
    - If the question id <= 0 or question id > assesments max questions, a 400 status is returned.
    """
    def get(self, request, pk, q_id, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.active:
            return Response({"message": "not allowed access questions for inactive instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to get question for a finished instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        questions = instance.assesment.question_set.all()
        if q_id <= 0 or q_id > len(questions):
            return Response({"message": "invalid question id"}, status=status.HTTP_400_BAD_REQUEST)
        question = questions[q_id - 1]
        question_serializer = QuestionSerializer(question, context={'request': request})
        return Response(question_serializer.data, status=status.HTTP_200_OK)


class InstanceAnswer(APIView):
    """ 
    From this endpoint you can send an answer for an assesment referencing the instance.

    Here is an example for sending an answer:
        
    {
        "question_id": 1,
        "option_id": 2
    }        

    If the answer is correctly saved, a response body like this is returned:

    {
        "message": "success", 
        "remaining_seconds": 3300
    }

    Here are some possibilities which don't save an answer in database
    - If the instance does not exists a 404 status is returned.
    - If the instance is inactive a 405 status is returned.
    - If the question_id or option_id are not integers a 400 status is returned.
    - If the question_id does not match with assesment or option does not match with question, a 400 status is returned
    """
    def put(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.active:
            return Response({"message": "not allowed answer questions for inactive instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to answer a question for a finished instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        question_id = request.data.get('question_id')
        option_id = request.data.get('option_id')
        if not isinstance(question_id, int) or not isinstance(option_id, int):
            return Response({"message": "question_id and option_id must be integers"}, status=status.HTTP_400_BAD_REQUEST)
        
        question = instance.assesment.question_set.filter(pk=question_id).first()
        if not question:
            return Response({"message": "question does not exists for the assesment"}, status=status.HTTP_400_BAD_REQUEST)
        
        option = question.option_set.filter(pk=option_id).first()
        if not option:
            return Response({"message": "option does not exists for the question"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(instance.progress_status, dict):
            instance.progress_status = dict()
        instance.progress_status[question_id] = option_id
        instance.save()
        return Response({"message": "success", "remaining_seconds": instance.remaining_seconds}, status=status.HTTP_200_OK)


class InstanceEnd(APIView):
    """
    From this endpoint you can end an instance, if the instance is activated.
    If the instance is not activated a 405 status is returned.
    """
    def post(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.active:
            return Response({"message": "only activated instances can be ended"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to finalize an instance again"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.end_time = timezone.now()
        instance.active = False
        instance.finalized = True
        instance.score = instance.calculate_score()
        instance.save()
        return Response({"message": "success", "result": reverse('assesments:instance-result', args=[pk], request=request, format=format)}, status=status.HTTP_200_OK)


class InstanceResult(APIView):
    """
    From this endpoint you can get an instance result and its taker.
    """
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.finalized:
            return Response({"message": "not possible to show result for non finalized instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.active:
            return Response({"message": "not possible to show result for an active instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('score', 'assesment', 'taker'))
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class InstanceRestore(APIView):
    """
    From this endpoint you can restore an instance details from another browser and get its progress.

    Here is an example for restore an instance based in a taker data:
        
    {
        "first_name": "Guido",
        "last_name": "Van Rossum",
        "email": "guido@python.org"
    }       

    Here are some not success possibilities:
    - If the instance taker data is invalid, a 400 status is returned.
    - If the taker has not active instance, a message informing it and 200 status is returned.
    """
    def post(self, request, format=None):
        taker_serializer = TakerSerializer(data=request.data)
        if not taker_serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        
        current_instance = Instance.objects.filter(
            taker__email=taker_serializer.validated_data['email'], active=True, finalized=False).first()
        if not current_instance:
            return Response({"message": "user has not active assesment instances"}, status=status.HTTP_200_OK)

        instance_serializer = InstanceSerializer(current_instance, context={'request': request}, fields=('url', 'duration', 'end_date', 'assesment', 'taker', 'remaining_seconds'))
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class TakerList(generics.ListAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TakerDetail(generics.RetrieveAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class OptionList(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OptionDetail(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
