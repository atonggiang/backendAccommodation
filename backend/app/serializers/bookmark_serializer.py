from rest_framework import serializers
from ..models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='user.profile.name', read_only=True)
    post_location = serializers.CharField(source='post.get_post_location', read_only=True)
    post_link = serializers.HyperlinkedRelatedField(
        source='post',
        read_only=True,
        view_name='post-detail'
    )
    class Meta:
        model = Bookmark
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
        }