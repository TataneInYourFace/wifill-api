from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.permissions.user import IsGetOrIsAdmin
from app.serializers.gas import GasSerializer
from app.models.gas import Gas


class GasViewSet(ModelViewSet):
    serializer_class = GasSerializer
    queryset = Gas.objects.all()
    permission_classes = (IsAuthenticated, IsGetOrIsAdmin)



