from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Confirm


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_fields = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20, write_only=True)


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirm
        fields = ('confirm',)
