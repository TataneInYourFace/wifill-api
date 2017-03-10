from rest_framework import serializers

from app.models import User
from app.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 'user', 'name', 'city', 'street', 'zip')
