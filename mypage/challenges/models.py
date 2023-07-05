from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    month = models.CharField(max_length=9)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.title} - {self.description} ({self.month}'s challenge with {self.rating} rating)"