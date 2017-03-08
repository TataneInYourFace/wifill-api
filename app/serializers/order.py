from rest_framework import serializers
from app.models.address import Address
from app.models.user import User
from app.models.vehicle import Vehicle
from app.models.order import Order
from app.serializers.address import AddressSerializer
from app.serializers.user import UserSerializer
from app.serializers.vehicle import VehicleSerializer
from app.serializers.join_renderer import PrimaryKeyGetWholeField


class OrderSerializer(serializers.ModelSerializer):
    address = PrimaryKeyGetWholeField(many=False, required=True, class_name=Address, class_serializer=AddressSerializer)
    vehicle = PrimaryKeyGetWholeField(many=False, required=True, class_name=Vehicle, class_serializer=VehicleSerializer)
    user = PrimaryKeyGetWholeField(many=False, required=True, class_name=User, class_serializer=UserSerializer)

    class Meta:
        model = Order
        fields = (
            'gaz_name', 'gaz_quantity', 'gaz_price', 'date_refill', 'date_created',
            'address', 'vehicle', 'user',)
