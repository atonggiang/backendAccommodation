from django.db import models 
from . import Room

class Picture(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='pics')  
    picture = models.FileField()