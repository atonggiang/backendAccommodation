from rest_framework import serializers
from ..models import Report

class ReportSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.profile.name', read_only=True)
    class Meta:
        model = Report
        exclude = []
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True},
        }