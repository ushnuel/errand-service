from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    phone = models.IntegerField()
    text = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author
