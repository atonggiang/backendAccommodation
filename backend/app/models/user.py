from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .. import managers

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Username', max_length=255, default='Nguyen Van A', unique=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
    is_superuser = models.BooleanField(verbose_name='Is Superuser', default=False)
    last_login = models.DateTimeField(verbose_name='Last Login', null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='Joined Since', auto_now_add=True)
    MODERATOR = 'M'
    OWNER = 'O'
    RENTER = 'R'
    ROLE_CHOICES = (
        (MODERATOR, 'Moderator'),
        (OWNER, 'Owner'),
        (RENTER, 'Renter'),
    )
    role = models.CharField(verbose_name='Role of User', max_length=1, default=RENTER, choices=ROLE_CHOICES)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = managers.UserManager()
    moder = managers.Moder()
    owner = managers.Owner()
    renter = managers.Renter()
    def __str__(self):
        return self.username
    # def save(self, *args, **kwargs): # this function is stupid since the only thing it does is to change the password everytime it is created or updated
    #     self.set_password(self.password)
    #     super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "user"
        ordering = ['-date_joined',]
        