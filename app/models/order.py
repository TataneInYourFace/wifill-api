from django.db import models

from app.models.gas import Gas
from app.models.user import User
from app.models.vehicle import Vehicle
from app.models.address import Address


class Order(models.Model):
    user = models.ForeignKey(User)
    vehicle = models.ForeignKey(Vehicle)
    address = models.ForeignKey(Address)

    gas_name = models.CharField(max_length=255, blank=False)
    gas_price = models.FloatField(blank=False)
    gas_quantity = models.IntegerField(blank=False)
    date_refill = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    is_payed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    class Meta:
        ordering = ('user', 'date_created',)
