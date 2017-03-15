"""wefill_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers


def get_swagger_view(title):
    class SwaggerSchemaView(APIView):
        permission_classes = [AllowAny]
        renderer_classes = [
            renderers.OpenAPIRenderer,
            renderers.SwaggerUIRenderer
        ]

        def get(self, request):
            generator = SchemaGenerator(title=title)
            schema = generator.get_schema()

            return Response(schema)
    return SwaggerSchemaView.as_view()

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('app.urls')),
    url(r'^api/docs/$', schema_view)
]
