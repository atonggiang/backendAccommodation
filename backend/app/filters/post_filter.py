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
    room_type = filters.CharFilter(field_name="room__room_type", lookup_expr='exact')
    bathroom_type = filters.CharFilter(field_name="room__bathroom_type", lookup_expr='exact')
    bathroom_heater = filters.BooleanFilter(field_name="room__bathroom_heater", lookup_expr='exact')
    kitchen_type = filters.CharFilter(field_name="room__kitchen_type", lookup_expr='exact')
    air_conditional = filters.BooleanFilter(field_name="room__air_conditional", lookup_expr='exact')
    balcony = filters.BooleanFilter(field_name="room__balcony", lookup_expr='exact')
    price_renter_to_pay__gt = filters.NumberFilter(field_name='room__price_renter_to_pay', lookup_expr='gte')
    price_renter_to_pay__lt = filters.NumberFilter(field_name='room__price_renter_to_pay', lookup_expr='lte')
    class Meta:
        model = models.Post
        exclude = ['room', 'display_duration_type', 'date_posted', 'verify_status']