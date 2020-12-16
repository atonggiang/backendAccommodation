from rest_framework import serializers
from ..models import Post
from .profile_serializer import ProfileSerializer
from .comment_serializer import CommentSerializer
from .review_serializer import ReviewSerializer

class PostSerializer(serializers.ModelSerializer):
    price_owner_to_pay = serializers.CharField(source='get_price_owner_pay', read_only=True)
    owner_profile = ProfileSerializer(source='user.profile', read_only=True)
    comments_in_this_post = CommentSerializer(many=True, source='get_verified_comments', read_only=True)
    reviews_in_this_post = ReviewSerializer(many=True, source='get_verified_reviews', read_only=True)
    total_likes_in_this_post = serializers.CharField(source='get_likes_count', read_only=True)
    total_bookmarks_in_this_post = serializers.CharField(source='get_bookmarks_count', read_only=True)
    class Meta:
        model = Post
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
        }