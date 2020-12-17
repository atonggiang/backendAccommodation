from rest_framework import viewsets
from .. import models
from .. import serializers

class ModeratorViewSet(viewsets.ModelViewSet):
    queryset = models.User.moder.all()
    serializer_class = serializers.UserSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = models.User.owner.all()
    serializer_class = serializers.UserSerializer

class RenterViewSet(viewsets.ModelViewSet):
    queryset = models.User.renter.all()
    serializer_class = serializers.UserSerializer
