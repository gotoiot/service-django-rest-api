from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from assesments.models import Assesment, Instance, Taker, Question, Option
from assesments.serializers import AssesmentSerializer, InstanceSerializer, TakerSerializer, QuestionSerializer, OptionSerializer


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