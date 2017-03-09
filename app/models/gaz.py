from django.db import models


class Gaz(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(blank=False)
    is_valide = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
