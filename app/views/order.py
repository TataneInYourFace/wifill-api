import datetime
import re
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from app.serializers.order import OrderSerializer
from app.models.order import Order
from app.views.simple_modelview import SimpleModelViewSet


class OrderViewSet(SimpleModelViewSet):

    model_class = Order
    serializer_class = OrderSerializer

    def list(self, request):
        q = Q()
        if "start_date" in request.query_params:
            if not re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", request.query_params.get("start_date")):
                return Response({"errors": "start_date should have YYYY-MM-DD format"},
                                status=status.HTTP_400_BAD_REQUEST)
            split = request.query_params.get("start_date").split("-")
            q &= Q(date_refill__gte=datetime.date(int(split[0]), int(split[1]), int(split[2])))
        if "end_date" in request.query_params:
            if not re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", request.query_params.get("end_date")):
                return Response({"errors": "end_date should have YYYY-MM-DD format"},
                                status=status.HTTP_400_BAD_REQUEST)
            split = request.query_params.get("end_date").split("-")
            q &= Q(date_refill__lte=datetime.date(int(split[0]), int(split[1]), int(split[2])))
        if request.user.is_admin:
            models = self.model_class.objects.filter(q)
        else:
            models = self.model_class.objects.filter(q)
        if models is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(models, many=True)
        return Response(serializer.data)


