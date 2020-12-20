from django.contrib.auth import authenticate
from rest_framework import serializers
from ..models import User
from .profile_serializer import ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='profile', read_only=True)
    class Meta:
        model = User
        exclude = [
            'is_active', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions',
        ]
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'user': {'write_only': True},
            'post': {'write_only': True},
        }
    #create user using custom save
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(max_length=1, read_only=True)
    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        return {
            'username':user.username,
            'role':user.role
        }