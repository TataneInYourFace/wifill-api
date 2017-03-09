from rest_framework.permissions import IsAuthenticated

from app.permissions.user import IsGetOrIsAdmin
from app.serializers.gaz import GazSerializer
from app.models.gaz import Gaz
from app.views.simple_modelview import SimpleModelViewSet


class GazViewSet(SimpleModelViewSet):

    model_class = Gaz
    serializer_class = GazSerializer
    is_related_to_user = False
    permission_classes = (IsAuthenticated, IsGetOrIsAdmin)



