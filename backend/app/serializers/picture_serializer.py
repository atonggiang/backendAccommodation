from rest_framework import serializers
from ..models import Picture

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        exclude = []
        extra_kwargs = {
            'room': {'write_only': True},
        }