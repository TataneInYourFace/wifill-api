from django.db import models
from .user_model import User
from .vehicle_model import Vehicle
from .address_model import Address


class Order(models.Model):
    user = models.ForeignKey(User)
    vehicle = models.ForeignKey(Vehicle)
    address = models.ForeignKey(Address)

    gaz_name = models.CharField(max_length=255, blank=False)
    gaz_quantity = models.IntegerField(blank=False)
    gaz_price = models.IntegerField(blank=False)
    date_refill = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('user', 'date_created',)
