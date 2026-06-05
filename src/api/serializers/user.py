from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email")