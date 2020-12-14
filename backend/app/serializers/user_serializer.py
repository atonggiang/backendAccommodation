from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'groups', 'user_permissions',
        ]
    #create user using custom save
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user