from django_filters import rest_framework as filters
from .. import models

class PostFilter(filters.FilterSet):
    is_available__exact = filters.BooleanFilter(field_name="room__is_available", lookup_expr='exact')
    address_number__exact = filters.NumberFilter(field_name="room__address_number", lookup_expr='exact')
    address_street__icontains = filters.CharFilter(field_name="room__address_street", lookup_expr='icontains')
    address_district__icontains = filters.CharFilter(field_name="room__address_district", lookup_expr='icontains')
    address_city = filters.CharFilter(field_name="room__address_city", lookup_expr='icontains')
    area__gt = filters.NumberFilter(field_name='room__area', lookup_expr='gte')
    area__lt = filters.NumberFilter(field_name='room__area', lookup_expr='lte')
    class Meta:
        model = models.Post
        exclude = ['room', 'display_duration_type', 'date_posted', 'verify_status']