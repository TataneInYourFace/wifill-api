from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from app.models.address import Address
from app.models.user import User
from app.models.vehicle import Vehicle
from app.models.order import Order
from app.serializers import AddressSerializer, VehicleSerializer, UserSerializer


class PrimaryKeyGetWholeField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.class_name = kwargs.pop("class_name", None)
        self.class_serializer = kwargs.pop("class_serializer", None)
        super().__init__(**kwargs)

    def get_queryset(self):
        return self.class_name.objects.all()

    def to_representation(self, value):
        model = self.class_name.objects.get(id=value.pk)
        serializer = self.class_serializer(model)
        return serializer.data


class OrderSerializer(serializers.ModelSerializer):
    address = PrimaryKeyGetWholeField(many=False, required=True, class_name=Address, class_serializer=AddressSerializer)
    vehicle = PrimaryKeyGetWholeField(many=False, required=True, class_name=Vehicle, class_serializer=VehicleSerializer)
    user = PrimaryKeyGetWholeField(many=False, required=True, class_name=User, class_serializer=UserSerializer)

    class Meta:
        model = Order
        fields = (
            'gaz_name', 'gaz_quantity', 'gaz_price', 'date_refill', 'date_created',
            'address', 'vehicle', 'user',)
