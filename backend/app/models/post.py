from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='posts')
    address_number = models.CharField(verbose_name='House Number', max_length=4, blank=True, default=14)
    address_street = models.CharField(verbose_name='Street Address', max_length=100, blank=True, default='Vuong Thua Vu')
    address_district = models.CharField(verbose_name='District Address', max_length=100, blank=True, default='Thanh Xuan')
    address_city = models.CharField(verbose_name='City Address', max_length=100, blank=True, default='Ha Noi')
    date_posted = models.DateTimeField(verbose_name='Date Posted', auto_now_add=True)
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
    number_of_room = models.PositiveIntegerField(default=13)
    price_per_month = models.DecimalField(max_digits=5, decimal_places=2, default=25.99)
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

    #TODO electricity bill go here

    optional_furniture = models.CharField(max_length=255, default='specify here')

    #TODO picture fields go here

    WEEK = 'W'
    MONTH = 'M'
    QUATER = 'Q'
    YEAR = 'Y'
    DISPLAY_DURATION_TYPE = [
        (WEEK, 'A Week'),
        (MONTH, 'A Month'),
        (QUATER, 'A Quater'),
        (YEAR, 'A Year'),
    ]
    display_duration_type = models.CharField(max_length=2, choices=DISPLAY_DURATION_TYPE, default=WEEK)
    display_duration_time = models.IntegerField(default=1)

    

    #TODO duration price code go here

    PENDING = 'P'
    APPROVED = 'A'
    DECLINED = 'D'
    VERIFY_STATUS = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DECLINED, 'Declined'),
    ]
    verify_status = models.CharField(verbose_name='Verify Status', max_length=1, choices=VERIFY_STATUS, default=PENDING)

    is_available = models.BooleanField(verbose_name='Is Available', default=True)

    # def __str__(self):
    #     return self.user.username
    
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "post"
        ordering = ['-date_posted',]
