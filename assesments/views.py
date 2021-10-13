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


def _get_model_by_pk(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'assesments': reverse('assesments:assesment-list', request=request, format=format),
        'instances': reverse('assesments:instance-list', request=request, format=format),
        'takers': reverse('assesments:taker-list', request=request, format=format),
        # 'questions': reverse('assesments:question-list', request=request, format=format),
        # 'options': reverse('assesments:option-list', request=request, format=format),
    })


class AssesmentList(generics.ListCreateAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AssesmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class InstanceList(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class InstanceCreate(APIView):
    def post(self, request, pk, format=None):
        """ Create and assesment instance based in assesment ID.
        If user data is invalid an is returned.
        If user has an active instance an is returned.
        If taker has an inactive instance for an assesment, the instance ID is returned
        instead of creating a new one.
        """
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
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        instance_serializer = InstanceSerializer(instance, context={'request': request})
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class InstanceStart(APIView):
    def post(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if instance.active:
            return Response({"message": "instance was already activated"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.start_time = timezone.now()
        instance.end_time = instance.start_time + datetime.timedelta(minutes=instance.duration)
        instance.active = True
        instance.save()
        instance_serializer = InstanceSerializer(instance, context={'request': request}, fields=('id', 'url', 'active', 'duration', 'start_date', 'end_date'))
        return Response(instance_serializer.data, status=status.HTTP_200_OK)


class InstanceQuestionDetail(APIView):
    def get(self, request, pk, q_id, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.active:
            return Response({"message": "not allowed access questions for inactive instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        questions = instance.assesment.question_set.all()
        if q_id <= 0 or q_id > len(questions):
            return Response({"message": "invalid question id"}, status=status.HTTP_400_BAD_REQUEST)
        question = questions[q_id - 1]
        question_serializer = QuestionSerializer(question, context={'request': request})
        return Response(question_serializer.data, status=status.HTTP_200_OK)


class InstanceAnswer(APIView):
    def put(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        if not instance.active:
            return Response({"message": "not allowed answer questions for inactive instance"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
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
        
        instance.progress_status[question_id] = option_id
        instance.save()
        return Response({"message": "success"}, status=status.HTTP_202_ACCEPTED)


class TakerList(generics.ListCreateAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taker.objects.all()
    serializer_class = TakerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class OptionList(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
