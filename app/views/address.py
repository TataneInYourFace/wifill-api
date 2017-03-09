from app.serializers.address import AddressSerializer
from app.models.address import Address
from app.views.simple_modelview import SimpleModelViewSet


class AddressViewSet(SimpleModelViewSet):

    model_class = Address
    serializer_class = AddressSerializer

