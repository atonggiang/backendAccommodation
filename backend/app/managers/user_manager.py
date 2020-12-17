from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

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

class Moder(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='M')

class Owner(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='O')

class Renter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='R')