from django.contrib import admin
from .import models 

# Register your models here.
admin.site.register(models.Room)
admin.site.register(models.Post)
admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Review)
admin.site.register(models.Like)
admin.site.register(models.Bookmark)
admin.site.register(models.Comment)
admin.site.register(models.Report)
admin.site.register(models.Picture)