from django_filters import rest_framework as filters
from .. import models

class PostFilter(filters.FilterSet):
    class Meta:
        model = models.Post
        exclude = []