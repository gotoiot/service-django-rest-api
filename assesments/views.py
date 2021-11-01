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
from rest_framework.decorators import api_view, permission_classes

from assesments.permissions import IsInstanceOwner
from assesments.models import Assesment, Instance, Option, Question, Taker
from assesments.serializers import (AssesmentSerializer, InstanceSerializer,
                                    OptionSerializer, QuestionSerializer,
                                    TakerSerializer)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated | permissions.IsAdminUser])
def api_root(request, format=None):
    """
    This is the main entry point for the Assesment app.
    From this endpoint you can explore each resources by clicking in each link below.
    """
    # Read taker as api user to don't depend of two models to determine the same
    api_user = Taker.objects.filter(user=request.user).first()

    response = {
        'assesments': reverse('assesments:assesment-list', request=request, format=format),
        'instances': reverse('assesments:instance-list', request=request, format=format)
    }
    if api_user.user.is_superuser or api_user.user.is_staff:
        response['takers'] = reverse('assesments:taker-list', request=request, format=format)
        response['questions'] = reverse('assesments:question-list', request=request, format=format)
        response['options'] = reverse('assesments:option-list', request=request, format=format)
    return Response(response, status=status.HTTP_200_OK)


class AssesmentList(generics.ListAPIView):
    """
    From this endpoint you can get the list of assesments.
    """
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]


class AssesmentDetail(APIView):
    """
    From this endpoint you can get the details of assesments created.
    """
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]

    def get(self, request, pk, format=None):
        assesment = get_object_or_404(Assesment, pk=pk)
        assesment_serializer = AssesmentSerializer(assesment, context={'request': request})
        response_data = {
            "next": reverse('assesments:instance-creation', args=[assesment.id], request=request, format=format),
        }
        response_data.update(assesment_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


class AssesmentStatus(APIView):
    """
    From this endpoint you can get the assesment status based in its id.
    """
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]

    def get(self, request, pk, format=None):
        _ = get_object_or_404(Assesment, pk=pk)
        return Response({"message": "success"}, status=status.HTTP_200_OK)


class InstanceList(generics.ListAPIView):
    """
    From this endpoint you can get the list of instances created.
    """
    serializer_class = InstanceSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]

    def get_queryset(self) :
        taker = Taker.objects.filter(user=self.request.user).first()
        if taker.user.is_superuser or taker.user.is_staff:
            return Instance.objects.all()
        return Instance.objects.filter(taker=taker)


class InstanceDetail(generics.RetrieveAPIView):
    """
    From this endpoint you can get the details of instances created.
    """
    serializer_class = InstanceSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]

    def get_queryset(self) :
        taker = Taker.objects.filter(user=self.request.user).first()
        if taker.user.is_superuser or taker.user.is_staff:
            return Instance.objects.all()
        return Instance.objects.filter(taker=taker)


class InstanceCreate(APIView):
    """ 
    From this endpoint you can create and assesment instance based in assesment ID.
    You must be logged in and have to make a POST to this endpoint in order to 
    create an instance. Just follow 'next' after creation.
    
    Here are some possibilities which won't create new instances:
    - If user is admin or staff
    - If user has an active instance a 405 status is returned.
    - If taker has an inactive instance for an assesment, the instance ID is returned instead of creating a new one.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        assesment = get_object_or_404(Assesment, pk=pk)

        taker = Taker.objects.filter(user=request.user).first()
        if taker.user.is_superuser or taker.user.is_staff:
            return Response({"message": "staff or admin users can't take assesments"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if taker.instance_set.filter(active=True).count() > 0:
            return Response({"message": "taker has active(s) test instance(s)"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if taker.instance_set.filter(active=False, finalized=False, assesment=assesment).count() > 0:
            instance = taker.instance_set.filter(active=False, finalized=False, assesment=assesment).first()
        else:
            instance = Instance(taker=taker, assesment=assesment, start_date=timezone.now(), end_date=timezone.now())
            instance.save()
        
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url'))
        response_data = {
            "next": reverse('assesments:instance-test', args=[instance.id], request=request, format=format),
        }
        response_data.update(instance_serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED)


class InstanceTest(APIView):
    """
    From this endpoint you can test if an instance is OK to be initiated.
    """
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]

    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url', 'active', 'finalized'))
        response_data = {
            "next": reverse('assesments:instance-start', args=[instance.id], request=request, format=format),
        }
        response_data.update(instance_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


class InstanceStart(APIView):
    """
    From this endpoint you can start an instance, if the instance is not activated.
    If the instance is activated a 405 status is returned.
    """
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]
    
    def post(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
        if instance.active:
            return Response({"message": "instance was already activated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to start a finished instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.start_date = timezone.now()
        instance.end_date = instance.start_date + datetime.timedelta(minutes=instance.duration)
        instance.active = True
        instance.save()
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url', 'active', 'duration', 'start_date', 'end_date'))
        response_data = {
            "next": reverse('assesments:instance-question-detail', args=[instance.id, instance.get_next_question_index()], request=request, format=format),
        }
        response_data.update(instance_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


class InstanceQuestionDetail(APIView):
    """
    From this endpoint you can get the question details for a selected question of an assesment instance.
    Here are some possible errors:
    - If the instance is inactive a 405 status is returned.
    - If the question id <= 0 or question id > assesments max questions, a 400 status is returned.
    """
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]
    
    def get(self, request, pk, q_id, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
        if not instance.active:
            return Response({"message": "not allowed access questions for inactive instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to get question for a finished instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        questions = instance.assesment.question_set.all()
        if q_id <= 0 or q_id > len(questions):
            return Response({"message": "invalid question id"}, status=status.HTTP_400_BAD_REQUEST)
        instance.question_index = q_id
        instance.save()
        question = questions[q_id - 1]
        question_serializer = QuestionSerializer(question, context={'request': request})
        response_data = {
            "next": reverse('assesments:instance-answer', args=[instance.id], request=request, format=format),
        }
        response_data.update(question_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


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
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]
    
    def put(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
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

        if instance.question_index >= instance.assesment.question_count:
            next_value = reverse('assesments:instance-end', args=[instance.id], request=request, format=format)
        else:
            next_value = reverse('assesments:instance-question-detail', args=[instance.id, instance.get_next_question_index()], request=request, format=format)
        response_data = {
            "message": "success", 
            "remaining_seconds": instance.remaining_seconds,
            "next": next_value,
            "prev": reverse('assesments:instance-question-detail', args=[instance.id, instance.get_prev_question_index()], request=request, format=format),
        }
        return Response(response_data, status=status.HTTP_200_OK)


class InstanceEnd(APIView):
    """
    From this endpoint you can end an instance, if the instance is activated.
    If the instance is not activated a 405 status is returned.
    """
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]
    
    def post(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
        if not instance.active:
            return Response({"message": "only activated instances can be ended"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.finalized:
            return Response({"message": "not possible to finalize an instance again"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.end_time = timezone.now()
        instance.active = False
        instance.finalized = True
        instance.score = instance.calculate_score()
        instance.save()

        response_data = {
            "message": "success", 
            "next": reverse('assesments:instance-result', args=[pk], request=request, format=format)
        }
        return Response(response_data, status=status.HTTP_200_OK)


class InstanceResult(APIView):
    """
    From this endpoint you can get an instance result and its taker.
    """
    permission_classes = [permissions.IsAuthenticated, IsInstanceOwner]
    
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        self.check_object_permissions(request, instance)
        if not instance.finalized:
            return Response({"message": "not possible to show result for non finalized instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if instance.active:
            return Response({"message": "not possible to show result for an active instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('score', 'assesment', 'taker'))
        response_data = {
            "next": reverse('assesments:instance-list', request=request, format=format),
        }
        response_data.update(instance_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


class InstanceRestore(APIView):
    """
    From this endpoint you can restore an instance in the same step you abandon it.
    You must be logged, have active and not finalized assesment instance.

    Here are some not success possibilities:
    - If you are admin or staff you can't restore an instance
    - If the taker has not active instance, a message informing it and 200 status is returned.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        taker = Taker.objects.filter(user=request.user).first()
        if taker.user.is_superuser or taker.user.is_staff:
            return Response({"message": "staff or admin users can't restore assesments"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        current_instance = Instance.objects.filter(taker=taker, active=True, finalized=False).first()
        if not current_instance:
            return Response({"message": "taker has not active assesment instances"}, status=status.HTTP_200_OK)

        instance_serializer = InstanceSerializer(current_instance, context={'request': request}, fields=('url', 'duration', 'end_date', 'assesment', 'taker', 'remaining_seconds'))
        response_data = {
            "next": reverse('assesments:instance-question-detail', args=[current_instance.id, current_instance.get_next_question_index()], request=request, format=format)
        }
        response_data.update(instance_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)


class TakerList(generics.ListAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    permission_classes = [permissions.IsAdminUser]


class TakerDetail(generics.RetrieveAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    permission_classes = [permissions.IsAdminUser]


class TakerDetailMeAnswer(APIView):
    """ 
    From this endpoint you can get your own taker details.
    The fields you can modify are: "age", "experience_years", "current_position", "mobile_phone", "profile", "genre", "nationality".

    Here is an example:
    {
        "age": 25,
        "experience_years": 10,
        "current_position": "Dev",
        "mobile_phone": "1126489293",
        "profile": "www.linkedin.com",
        "genre": "m",
        "nationality": "AR"
    }
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        taker = Taker.objects.filter(user=request.user).first()
        taker_serializer = TakerSerializer(taker, context={'request': request})
        return Response(taker_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        taker = Taker.objects.filter(user=request.user).first()
        taker_serializer = TakerSerializer(taker, data=request.data, context={'request': request})
        if not taker_serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        taker_serializer.save()
        return Response(taker_serializer.data, status=status.HTTP_200_OK)


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class OptionList(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAdminUser]


class OptionDetail(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAdminUser]
