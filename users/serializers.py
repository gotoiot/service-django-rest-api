from rest_framework import serializers

from users.models import ApiUser


class ApiUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiUser
        fields = ['id', 'email', 'first_name', 'last_name']