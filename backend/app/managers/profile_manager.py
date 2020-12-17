from django.db import models 

class ProfileVerified(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_verified=True)

class ProfileNotVerified(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_verified=False)