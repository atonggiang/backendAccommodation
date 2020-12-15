from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'is_active', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions',
        ]
        extra_kwargs = {
            'date_joined': {'read_only': True}
        }
    #create user using custom save
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user