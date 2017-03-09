from app.serializers.order import OrderSerializer
from app.models.order import Order
from app.views.simple_modelview import SimpleModelViewSet


class OrderViewSet(SimpleModelViewSet):

    model_class = Order
    serializer_class = OrderSerializer

