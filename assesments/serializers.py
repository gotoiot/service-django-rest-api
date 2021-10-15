from rest_framework import serializers
from django.contrib.auth.models import User

from assesments.models import Assesment, Instance, Taker, Question, Option


class AssesmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assesment
        fields = ('url', 'id', 'created', 'title', 'description', 'language', 'question_count', 'thanks_message',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:assesment-detail', 'lookup_field': 'pk'},
        }


class TakerSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(TakerSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        taker = Taker.objects.filter(email=validated_data['email']).first()
        if taker:
            if taker.first_name != validated_data['first_name'] or taker.last_name != validated_data['last_name']:
                raise serializers.ValidationError({"message": "The email registered and taker names do not match"})
            return taker
        return Taker.objects.create(**self.validated_data)

    class Meta:
        model = Taker
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'experience_years', 'current_position', 'mobile_phone', 'email', 'profile', 'genre', 'nationality',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:taker-detail', 'lookup_field': 'pk'},
        }


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    assesment = AssesmentSerializer()
    taker = TakerSerializer(fields=('id', 'first_name', 'last_name', 'email', 'url'))

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(InstanceSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Instance
        fields = ('url', 'id', 'duration', 'score', 'start_date', 'end_date', 'active', 'progress_status', 'assesment', 'taker')
        extra_kwargs = {
            'url': {'view_name': 'assesments:instance-detail', 'lookup_field': 'pk'},
        }
    

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(OptionSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Option
        fields = ('id', 'title', 'text', 'is_correct', 'option_type', 'url')
        extra_kwargs = {
            'url': {'view_name': 'assesments:option-detail', 'lookup_field': 'pk'},
        }


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    assesment = AssesmentSerializer()
    option_set = OptionSerializer(many=True, fields=('id', 'title', 'text', 'option_type', 'url'))

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'category', 'question_type', 'assesment', 'option_set', 'url')
        extra_kwargs = {
            'url': {'view_name': 'assesments:question-detail', 'lookup_field': 'pk'},
        }
