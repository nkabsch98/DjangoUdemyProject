from django.db import models

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    month = models.CharField(max_length=9)
    rating = models.IntegerField()