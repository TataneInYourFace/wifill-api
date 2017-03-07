from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from app.models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    address_id = PrimaryKeyRelatedField(many=False, read_only=True)
    vehicle_id = PrimaryKeyRelatedField(many=False, read_only=True)
    user_id = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Order
        fields = (
            'address', 'vehicle', 'user', 'gaz_name', 'gaz_quantity', 'gaz_price', 'date_refill', 'date_created',
            'address_id', 'vehicle_id', 'user_id')