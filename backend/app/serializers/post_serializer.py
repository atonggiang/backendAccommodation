from rest_framework import serializers
from ..models import Post
from .profile_serializer import ProfileSerializer
from .comment_serializer import CommentSerializer
from .review_serializer import ReviewSerializer
from .room_serializer import RoomSerializer

class PostSerializer(serializers.ModelSerializer):
    owner_profile = ProfileSerializer(source='room.user.profile', read_only=True)
    room_detail = RoomSerializer(source='room', read_only=True)
    price_owner_to_pay = serializers.CharField(source='get_price_owner_pay', read_only=True)
    comments_in_this_post = CommentSerializer(many=True, source='get_comments', read_only=True)
    reviews_in_this_post = ReviewSerializer(many=True, source='get_reviews', read_only=True)
    total_likes_in_this_post = serializers.CharField(source='get_likes_count', read_only=True)
    total_bookmarks_in_this_post = serializers.CharField(source='get_bookmarks_count', read_only=True)
    is_due_man = serializers.CharField(source='is_due', read_only=True)
    class Meta:
        model = Post
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
            'room': {'write_only': True},
            'date_posted': {'read_only': True},
        }