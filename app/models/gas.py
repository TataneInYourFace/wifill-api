from django.db import models


class Gas(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(blank=False)

    class Meta:
        ordering = ('name',)
