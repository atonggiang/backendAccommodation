from rest_framework import serializers
from ..models import Like

class LikeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.profile.name', read_only=True)
    class Meta:
        model = Like
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
        }