from django.conf.urls import url
from app.views.login import LoginView
from app.views.user import UserViewSet
from app.views.order import OrderViewSet
from app.views.address import AddressViewSet
from app.views.vehicle import VehicleViewSet
from app.views.gas import GasViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, "users")
router.register(r'orders', OrderViewSet, "orders")
router.register(r'addresses', AddressViewSet, "addresses")
router.register(r'vehicles', VehicleViewSet, "vehicles")
router.register(r'gas', GasViewSet, "gas")


urlpatterns = [
    url(r'^users/login/$', LoginView.as_view()),
]

urlpatterns += router.urls
