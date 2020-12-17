from rest_framework import viewsets
from .. import models
from .. import serializers

class ProfileVerifiedViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.verified.all()
    serializer_class = serializers.ProfileSerializer

class ProfileNotVerifiedViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.notverified.all()
    serializer_class = serializers.ProfileSerializer

