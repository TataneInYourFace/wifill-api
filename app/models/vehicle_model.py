from django.db import models
from .user_model import User


class Vehicle(models.Model):
    user = models.ForeignKey(User)

    plate = models.CharField(max_length=255, blank=False, unique=True)
    brand = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('user', 'brand',)
