from django.db import models
from app.models.user import User


class Address(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    zip = models.CharField(max_length=10, blank=False)

    class Meta:
        ordering = ('user', 'zip',)
