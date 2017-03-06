from app.models import User
from app.serializers.address import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    address_set = AddressSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'date_created', 'date_modified',
            'firstname', 'lastname', 'password', 'confirm_password', 'is_admin', 'address_set')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        addresses_data = {}
        if 'address_set' in validated_data:
            addresses_data = validated_data.pop('address_set')
        user = User.objects.create_user(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(user=user, **address_data)
        return user

    def update(self, instance, validated_data):
        addresses_data = {}
        if 'address_set' in validated_data:
            addresses_data = validated_data.pop('address_set')
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
        '''
        Ensure the passwords are the same
        '''
        if 'password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data
