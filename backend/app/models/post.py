from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from .. import constants
from . import Room
from .. import managers

# Create your models here.
class Post(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, verbose_name='Room Post', related_name='post')
    date_posted = models.DateTimeField(verbose_name='Date Posted', null=True)
    display_duration_type = models.CharField(verbose_name='Display Duration', max_length=2, choices=constants.DISPLAY_DURATION_TYPE, default=constants.WEEK)
    verify_status = models.CharField(verbose_name='Verify Status', max_length=1, choices=constants.VERIFY_STATUS, default=constants.PENDING)
    is_available = models.BooleanField(verbose_name='Is Available', default=True)
    objects = models.Manager()
    pending = managers.PendingPost()
    approved = managers.ApprovedPost()
    declined = managers.DeclinedPost()
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "post"
        ordering = ['-date_posted',]
    def get_price_owner_pay(self):
        if self.display_duration_type == constants.WEEK:
            return constants.WEEK_PRICE
        elif self.display_duration_type == constants.MONTH:
            return MONTH_PRICE
        elif self.display_duration_type == constants.QUATER:
            return constants.QUATER_PRICE
        else :
            return constants.YEAR_PRICE
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
    def get_location(self):
        address = '{address_number}, {address_street} Str, {address_district} District, {address_city} City'.format(
            address_number=self.room.address_number, 
            address_street=self.room.address_street, 
            address_district=self.room.address_district, 
            address_city=self.room.address_city)
        return address
    def set_post_pending(self):
        self.verify_status = constants.PENDING
        self.save(update_fields=['verify_status'])
    def approve_post_status(self):
        self.verify_status = constants.APPROVED
        self.date_posted = timezone.now() #then restart the date
        self.save(update_fields=['verify_status', 'date_posted'])
    def is_due(self):
        if self.verify_status != constants.APPROVED:
            return
        day_delta = 7
        if self.display_duration_type == constants.MONTH:
            day_delta = 30
        elif self.display_duration_type == constants.QUATER:
            day_delta = 120
        else :
            day_delta = 365
        return self.date_posted <= timezone.localtime(timezone.now()) - datetime.timedelta(days=day_delta)