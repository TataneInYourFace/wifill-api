from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from app.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    user = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Vehicle
        fields = (
            'id', 'plate', 'brand', 'name', 'color')


