from rest_framework import serializers
from app.models import User
from .address_serializer import *
import pprint


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    address_set = AddressSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'date_created', 'date_modified',
            'firstname', 'lastname', 'password', 'confirm_password', 'is_admin', 'address_set')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        addresses_data = validated_data.pop('address_set')
        user = User.objects.update_or_create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(user=user, **address_data)
        return user

    def update(self, instance, validated_data):
        pprint.pprint(validated_data)
        for attr, value in validated_data.items():
            print(attr)
            print(value)
            setattr(instance, attr, value)
        instance.save()
        print(instance)
        return instance

    # def to_internal_value(self, data):
    #     internal_value = super(UserSerializer, self).to_internal_value(data)
    #     for val in self.Meta.fields:
    #         if val in data:
    #             internal_value.update({
    #                 val: data.get(val)
    #             })
    #     return internal_value

    def validate(self, data):
        '''
        Ensure the passwords are the same
        '''
        print("lul")
        if 'password' in data:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data
