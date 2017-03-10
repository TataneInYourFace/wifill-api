from rest_framework import serializers
from app.models.gas import Gas


class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = (
            'id', 'name', 'price',)
