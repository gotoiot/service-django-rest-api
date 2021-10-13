from rest_framework import serializers
from django.contrib.auth.models import User

from assesments.models import Assesment, Instance, Taker, Question, Option


class AssesmentSerializer(serializers.HyperlinkedModelSerializer):
    # TODO find a way to get question count here
    class Meta:
        model = Assesment
        fields = ('url', 'id', 'created', 'title', 'description', 'language', 'thanks_message',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:assesment-detail', 'lookup_field': 'pk'},
        }


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    assesment = serializers.HyperlinkedRelatedField(view_name='assesments:assesment-detail', lookup_field='pk', read_only=True)
    taker = serializers.HyperlinkedRelatedField(view_name='assesments:taker-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = Instance
        fields = ('url', 'id', 'duration', 'score', 'start_date', 'end_date', 'active', 'progress_status', 'assesment', 'taker')
        extra_kwargs = {
            'url': {'view_name': 'assesments:instance-detail', 'lookup_field': 'pk'},
        }


class TakerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Taker
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'experience_years', 'current_position', 'mobile_phone', 'email', 'profile', 'genre', 'nationality',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:taker-detail', 'lookup_field': 'pk'},
        }

    def create(self, validated_data):
        taker = Taker.objects.filter(email=validated_data['email']).first()
        if taker:
            if taker.first_name != validated_data['first_name'] or taker.last_name != validated_data['last_name']:
                raise serializers.ValidationError("The email registered and taker names do not match")
            return taker
        return Taker.objects.create(**self.validated_data)


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