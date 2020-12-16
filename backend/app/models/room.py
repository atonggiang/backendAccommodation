from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='posts')
    address_number = models.CharField(verbose_name='House Number', max_length=4, blank=True, default=14)
    address_street = models.CharField(verbose_name='Street Address', max_length=100, blank=True, default='Vuong Thua Vu')
    address_district = models.CharField(verbose_name='District Address', max_length=100, blank=True, default='Thanh Xuan')
    address_city = models.CharField(verbose_name='City Address', max_length=100, blank=True, default='Ha Noi')
    HOUSE = 'H'
    STUDIO = 'S'
    APARTMENT = 'A'
    MINIROOM = 'M'
    ROOM_TYPE = [
        (HOUSE, 'House'),
        (STUDIO, 'Studio'),
        (APARTMENT, 'Apartment'),
        (MINIROOM, 'Miniroom'),
    ]
    room_type = models.CharField(max_length=2, choices=ROOM_TYPE, default=STUDIO)
    number_of_room = models.PositiveIntegerField(default=3)
    area = models.PositiveIntegerField(default=100)
    SHARED = 'S'
    PRIVATE = 'P'
    BATHROOM_TYPE = [
        (SHARED, 'Shared'),
        (PRIVATE, 'Private'),
    ]
    bathroom_type = models.CharField(max_length=2, choices=BATHROOM_TYPE, default=SHARED)
    bathroom_heater = models.BooleanField(default=False)
    NOKITCHEN = 'N'
    KITCHEN_TYPE = [
        (SHARED, 'Shared'),
        (PRIVATE, 'Private'),
        (NOKITCHEN, 'No Kitchen'),
    ]
    kitchen_type = models.CharField(max_length=2, choices=KITCHEN_TYPE, default=SHARED)
    air_conditional = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    water_electricity_bill_per_week = models.DecimalField(verbose_name='Bill for Water & Electricity per Week' ,max_digits=5, decimal_places=2, default=9.99)

    optional_furniture = models.CharField(verbose_name='More Option Furniture', max_length=255, default='specify here')

    #TODO picture fields go here


    # def __str__(self):
    #     return self.user.username
    
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "room"
    def get_location(self):
        address = '{address_number}, {address_street} Str, {address_district} District, {address_city} City'.format(
            address_number=self.address_number, 
            address_street=self.address_street, 
            address_district=self.address_district, 
            address_city=self.address_city)
        return address