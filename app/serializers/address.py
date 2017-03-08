from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from app.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    user = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Address
        fields = (
            'id', 'name', 'street', 'city', 'zip')


