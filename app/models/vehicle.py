from django.db import models
from app.models.user import User


class Vehicle(models.Model):
    user = models.ForeignKey(User, null=True)

    plate = models.CharField(max_length=255, blank=False)
    brand = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('user', 'brand',)
