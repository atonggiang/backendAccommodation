from django.db import models
from django.conf import settings
from .. import constants

# Create your models here.
class Room(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rooms')
    address_number = models.CharField(verbose_name='House Number', max_length=4, blank=True, default=14)
    address_street = models.CharField(verbose_name='Street Address', max_length=100, blank=True, default='Vuong Thua Vu')
    address_district = models.CharField(verbose_name='District Address', max_length=100, blank=True, default='Thanh Xuan')
    address_city = models.CharField(verbose_name='City Address', max_length=100, blank=True, default='Ha Noi')
    room_type = models.CharField(max_length=2, choices=constants.ROOM_TYPE, default=constants.STUDIO)
    number_of_room = models.PositiveIntegerField(default=3)
    area = models.PositiveIntegerField(default=100)
    bathroom_type = models.CharField(max_length=2, choices=constants.BATHROOM_TYPE, default=constants.SHARED)
    bathroom_heater = models.BooleanField(default=False)
    kitchen_type = models.CharField(max_length=2, choices=constants.KITCHEN_TYPE, default=constants.SHARED)
    air_conditional = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    water_electricity_bill_per_week = models.DecimalField(verbose_name='Bill for Water & Electricity per Week' ,max_digits=5, decimal_places=2, default=9.99)
    optional_furniture = models.CharField(verbose_name='More Option Furniture', max_length=255, default='specify here')
    is_available = models.BooleanField(verbose_name='Is Available', default=True)
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "room"
    def get_location(self):
        return '{address_number}, {address_street} Str, {address_district} District, {address_city} City'.format(
            address_number=self.address_number, 
            address_street=self.address_street, 
            address_district=self.address_district, 
            address_city=self.address_city)
