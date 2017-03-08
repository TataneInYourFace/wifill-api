from app.serializers.vehicle import VehicleSerializer
from app.models.vehicle import Vehicle
from app.views.simple_modelview import SimpleModelViewSet


class VehicleViewSet(SimpleModelViewSet):

    model_class = Vehicle
    serializer_class = VehicleSerializer

