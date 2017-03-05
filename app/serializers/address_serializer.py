from rest_framework import serializers
from app.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 'name', 'street', 'city', 'zip')
