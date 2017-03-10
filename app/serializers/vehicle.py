from rest_framework import serializers

from app.models import User
from app.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'id', 'user', 'plate', 'brand', 'name', 'color')


