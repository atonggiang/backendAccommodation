from rest_framework import serializers
from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
            'is_verified': {'write_only': True},
        }