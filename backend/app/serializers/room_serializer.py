from rest_framework import serializers
from ..models import Room
from .picture_serializer import PictureSerializer

class RoomSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.profile.name', read_only=True)
    pictures_included = PictureSerializer(
        many=True, 
        source='pics', 
        read_only=True,
    )
    class Meta:
        model = Room
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
        }