from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.profile.name', read_only=True)
    class Meta:
        model = Review
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
            'is_verified': {'write_only': True},
        }