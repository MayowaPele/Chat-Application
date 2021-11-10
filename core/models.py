from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room_id = models.CharField(max_length=100000)
    

    def __str__(self):
        return self.value