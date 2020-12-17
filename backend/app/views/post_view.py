from rest_framework import viewsets
from django_filters import rest_framework as filters
from .. import models
from .. import serializers
from ..filters import PostFilter

class PendingPostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.pending.all()
    serializer_class = serializers.PostSerializer

class ApprovedPostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.approved.all()
    serializer_class = serializers.PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

class DeclinedPostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.declined.all()
    serializer_class = serializers.PostSerializer
