from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from users.models import ApiUser

# TODO understand how to configure serializers

class ApiUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiUser
        fields = ['id', 'email', 'first_name', 'last_name']


class ApiUserRegistrationSerializer(RegisterSerializer):

    # Define transaction.atomic to rollback in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.save()
        return user