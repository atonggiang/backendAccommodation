from rest_framework import serializers
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
        }