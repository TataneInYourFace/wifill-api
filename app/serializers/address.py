from rest_framework import serializers
from app.models import Address


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)

    class Meta:
        model = Address
        fields = (
            'id', 'name', 'street', 'city', 'zip')


