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
    number_of_room = models.PositiveIntegerField(default=3)
    price_per_month = models.DecimalField(verbose_name='Price to pay per month', max_digits=5, decimal_places=2, default=25.99)
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

    bill_usage_per_hour = models.DecimalField(verbose_name='Water & Electricity Bill Per Hour', max_digits=5, decimal_places=2, default=19.99)

    optional_furniture = models.CharField(verbose_name='More Option Furniture', max_length=255, default='specify here')

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
    def get_price_owner_pay(self):
        WEEK_PRICE = 12.99
        MONTH_PRICE = 9.99
        QUATER_PRICE = 5.99
        YEAR_PRICE = 2.99
        if self.display_duration_type == 'W':
            return WEEK_PRICE
        elif self.display_duration_type == 'M':
            return MONTH_PRICE
        elif self.display_duration_type == 'Q':
            return QUATER_PRICE
        else :
            return YEAR_PRICE
    def get_bookmarks_count(self):
        return self.bookmarks_post.count()
    def get_likes_count(self):
        return self.likes_post.count()
    def get_verified_comments_count(self):
        return self.comments_post.filter(is_verified=True).count()
    def get_verified_comments(self):    
        return self.comments_post.filter(is_verified=True)
    def get_verified_reviews_count(self):
        return self.reviews_post.filter(is_verified=True).count()
    def get_verified_reviews(self):    
        return self.reviews_post.filter(is_verified=True)
    def get_post_location(self):
        address = '{address_number}, {address_street} Str, {address_district} District, {address_city} City'.format(
            address_number=self.address_number, 
            address_street=self.address_street, 
            address_district=self.address_district, 
            address_city=self.address_city)
        return address