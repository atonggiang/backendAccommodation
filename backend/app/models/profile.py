from django.db import models
from django.conf import settings
from .. import managers

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User Profile', related_name='profile')
    name = models.CharField(verbose_name='User Name', max_length=40, blank=True)
    id_card = models.CharField(verbose_name='Identification Number', max_length=14, blank=True)
    home_address = models.CharField(verbose_name='Home Address', max_length=255, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, blank=True)
    email = models.EmailField(verbose_name='Email Address', max_length=255, blank=True)
    is_verified = models.BooleanField(verbose_name='Is Verified', default=False)
    objects = models.Manager()
    verified = managers.ProfileVerified()
    notverified = managers.ProfileNotVerified()
    # def __str__(self):
    #     return self.user.username