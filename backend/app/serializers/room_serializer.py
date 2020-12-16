from rest_framework import serializers
from ..models import Room

class RoomSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.profile.name', read_only=True)
    pictures_included = serializers.HyperlinkedRelatedField(
        many=True, 
        source='pics', 
        read_only=True,
        view_name='picture-detail'
    )
    class Meta:
        model = Room
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
        }