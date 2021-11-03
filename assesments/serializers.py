from rest_framework import serializers

from users.serializers import ApiUserDetailSerializer
from assesments.models import Assesment, Instance, Taker, Question, Option


class AssesmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assesment
        fields = ('url', 'id', 'created', 'title', 'description', 'language', 'question_count', 'thanks_message',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:assesment-detail', 'lookup_field': 'pk'},
        }


class TakerSerializer(serializers.HyperlinkedModelSerializer):
    user = ApiUserDetailSerializer()

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(TakerSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def update(self, instance, validated_data): 
        instance.age = validated_data.get('age', instance.age)
        instance.experience_years = validated_data.get('experience_years', instance.experience_years)
        instance.current_position = validated_data.get('current_position', instance.current_position)
        instance.mobile_phone = validated_data.get('mobile_phone', instance.mobile_phone)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.save()
        return instance

    class Meta:
        model = Taker
        fields = ('url', 'user', 'id', 'age', 'experience_years', 'current_position', 'mobile_phone', 'profile', 'genre', 'nationality',)
        extra_kwargs = {
            'url': {'view_name': 'assesments:taker-detail', 'lookup_field': 'pk'},
        }


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    assesment = AssesmentSerializer()
    taker = TakerSerializer(fields=('id', 'url', 'user'))

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
        fields = ('url', 'id', 'duration', 'score', 'start_date', 'end_date', 'active', 'finalized', 'progress_status', 'assesment', 'taker', 'remaining_seconds')
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
