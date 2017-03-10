from rest_framework import serializers
from app.models.address import Address
from app.models.vehicle import Vehicle
from app.models.order import Order
from app.serializers.address import AddressSerializer
from app.serializers.vehicle import VehicleSerializer
from app.serializers.primary_key_on_get_whole import PrimaryKeyOnGetWholeField


class OrderSerializer(serializers.ModelSerializer):
    address = PrimaryKeyOnGetWholeField(many=False, required=True, class_name=Address,
                                        class_serializer=AddressSerializer)
    vehicle = PrimaryKeyOnGetWholeField(many=False, required=True, class_name=Vehicle,
                                        class_serializer=VehicleSerializer)

    class Meta:
        model = Order
        fields = (
            'id', 'gas_name', 'gas_price', 'gas_quantity', 'date_refill', 'date_created', 'is_payed', 'is_canceled',
            'address', 'vehicle', 'user')
