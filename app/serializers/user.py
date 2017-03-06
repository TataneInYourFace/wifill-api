import pprint

from rest_framework import serializers

from app.models import Address
from app.models import User
from app.models import Vehicle
from app.serializers.address import AddressSerializer
from app.serializers.vehicle import VehicleSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    address_set = AddressSerializer(many=True, required=False)
    vehicle_set = VehicleSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'date_created', 'date_modified',
            'firstname', 'lastname', 'password', 'confirm_password', 'is_admin')
        join_fields = {
            'address_set': Address,
            'vehicle_set': Vehicle
        }
        for key, value in join_fields.items():
            fields += (key,)
        read_only_fields = ('date_created', 'date_modified')

    def create_joins(self, validated_data):
        array = []
        for key, class_name in self.Meta.join_fields.items():
            if key in validated_data:
                array.append({
                    "class_name": class_name,
                    "data": validated_data.pop(key)
                })
        pprint.pprint(array)
        return array

    def create(self, validated_data):
        joins = self.create_joins(validated_data)
        user = User.objects.create_user(**validated_data)
        for value in joins:
            class_name = value.get("class_name")
            data = value.get("data")
            for obj in data:
                class_name.objects.create(user=user, **obj)
        return user

    def update(self, instance, validated_data):
        addresses_data = {}
        # joins = self.read_joins(validated_data)
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        addresses_ids = []
        address_set = Address.objects.filter(user=instance)
        for address in addresses_data:
            id_address = address.get("id")
            if id_address is not None:
                addresses_ids.append(id_address)
        for address in address_set:
            if address.id not in addresses_ids:
                address.delete()
        for address_data in addresses_data:
            Address.objects.create(user=instance, **address_data)
        return instance

    def validate(self, data):
        """
        Ensure the passwords are the same
        """
        if 'password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data
