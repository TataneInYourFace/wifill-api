from rest_framework import serializers
from app.models.gaz import Gaz


class GazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gaz
        fields = (
            'id', 'name', 'price',)
