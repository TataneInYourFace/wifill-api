import pprint

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.permissions.user import *


class SimpleModelViewSet(viewsets.ViewSet):

    is_related_to_user = True
    model_class = None
    permission_classes = (IsAuthenticated, IsOwnerOrIsAdmin,)
    serializer_class = None
    # Router class variables
    lookup_field = 'id'
    lookup_value_regex = '\d+'

    def retrieve(self, request, id=None):
        try:
            model = self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404
        if self.is_related_to_user:
            self.check_object_permissions(request, model)
        serializer = self.serializer_class(model)
        pprint.pprint(serializer.data)
        return Response(serializer.data)

    def list(self, request):
        if request.user.is_admin:
            if hasattr(self.model_class, 'is_valid'):
                models = self.model_class.objects.filter(is_valid=True)
            else:
                models = self.model_class.objects.all()
        else:
            if hasattr(self.model_class, 'is_valid'):
                models = self.model_class.objects.filter(user=request.user, is_valid=True)
            else:
                models = self.model_class.objects.filter(user=request.user)
        if models is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(models, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        try:
            model = self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404
        if self.is_related_to_user:
            self.check_object_permissions(request, model)
        serializer = self.serializer_class(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):
        try:
            model = self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise Http404
        if self.is_related_to_user:
            self.check_object_permissions(request, model)
            if hasattr(model, 'is_valid'):
                model.is_active = False
                model.save()
            else:
                model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
