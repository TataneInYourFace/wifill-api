from django.conf.urls import url
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, "users")


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^register/$', AuthRegister.as_view()),
]

urlpatterns += router.urls
