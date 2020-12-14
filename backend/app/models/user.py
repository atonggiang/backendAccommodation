from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)
    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)
    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

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
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()
    def __str__(self):
        return self.username
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "user"
        ordering = ['-date_joined',]
        