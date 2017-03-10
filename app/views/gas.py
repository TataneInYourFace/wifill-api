from rest_framework.permissions import IsAuthenticated

from app.permissions.user import IsGetOrIsAdmin
from app.serializers.gas import GasSerializer
from app.models.gas import Gas
from app.views.simple_modelview import SimpleModelViewSet


class GasViewSet(SimpleModelViewSet):

    model_class = Gas
    serializer_class = GasSerializer
    is_related_to_user = False
    permission_classes = (IsAuthenticated, IsGetOrIsAdmin)



