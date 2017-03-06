from rest_framework import serializers
from app.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Vehicle
        fields = (
            'id', 'plate', 'brand', 'name', 'color')


