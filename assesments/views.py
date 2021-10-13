from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, permissions, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils import timezone

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
        assesment = get_object_or_404(Assesment, pk=pk)
        taker_serializer = TakerSerializer(data=request.data)
        if not taker_serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        taker = taker_serializer.save()
        instance = Instance(taker=taker, assesment=assesment, start_date=timezone.now(), end_date=timezone.now())
        instance.save()
        instance_serializer = InstanceSerializer(instance, context={'request': request})
        return Response(instance_serializer.data, status=status.HTTP_201_CREATED)


class InstanceTest(APIView):
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        instance_serializer = InstanceSerializer(instance, context={'request': request})
        return Response(instance_serializer.data, status=status.HTTP_200_SUCCESS)


class InstanceStart(APIView):
    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        instance.start_time = timezone.now()
        instance.end_time = timezone.now() + timedelta(minutes=instance.duration)
        instance.active = True
        instance.save()
        first_question = instance.assesment.question_set.first()
        # TODO this response must be a Serializer data
        return Response({'uuid': instance.id, 'active': instance.active})


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
