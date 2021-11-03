from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, PasswordResetConfirmSerializer

from users.models import ApiUser


class ApiUserRegistrationSerializer(RegisterSerializer):
    username = None
    password1 = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})

    @transaction.atomic
    def save(self, request):
        """ Define transaction.atomic to rollback in case of error """
        user = super().save(request)
        user.save()
        return user


class ApiUserLoginSerializer(LoginSerializer):
    username = None


class ApiUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ['email']


class ApiUserPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    new_password1 = serializers.CharField(style={'input_type': 'password'})
    new_password2 = serializers.CharField(style={'input_type': 'password'})
