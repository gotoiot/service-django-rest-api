from rest_framework import serializers
from django.contrib.auth.models import User

from assesments.models import Assesment, Instance, Taker, Question, Option


class AssesmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Assesment
        fields = ('url', 'id', 'created', 'title', 'description', 'language', 'thanks_message',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:assesment-detail', 'lookup_field': 'pk'},
        }


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    # assesment = serializers.ReadOnlyField(source='assesment.url')
    # taker = serializers.ReadOnlyField(source='taker.url')

    class Meta:
        model = Instance
        fields = ('url', 'id', 'duration', 'score', 'start_date', 'end_date', 'active', 'progress_status')
        extra_kwargs = {
            'url': {'view_name': 'assesments:instance-detail', 'lookup_field': 'pk'},
        }


class TakerSerializer(serializers.HyperlinkedModelSerializer):
    # instances = serializers.ReadOnlyField(source='instance')

    class Meta:
        model = Taker
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'experience_years', 'current_position', 'mobile_phone', 'email', 'profile', 'genre', 'nationality',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:taker-detail', 'lookup_field': 'pk'},
        }


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    # assesment = serializers.ReadOnlyField(source='assesment.url')

    class Meta:
        model = Question
        fields = ('url', 'id', 'title', 'description', 'category', 'question_type', 'assesment')
        extra_kwargs = {
            'url': {'view_name': 'assesments:question-detail', 'lookup_field': 'pk'},
        }


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    # question = serializers.ReadOnlyField(source='question.url')

    class Meta:
        model = Option
        fields = ('url', 'id', 'title', 'text', 'is_correct', 'option_type', 'question')
        extra_kwargs = {
            'url': {'view_name': 'assesments:option-detail', 'lookup_field': 'pk'},
        }