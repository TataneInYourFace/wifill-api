import pprint

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.permissions.user import *
from app.serializers.address import AddressSerializer
from app.models.order import Order


class AddressViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated, IsOwnerOrIsAdmin,)
    serializer_class = AddressSerializer
    # Router class variables
    lookup_field = 'id'
    lookup_value_regex = '\d+'

    def list(self, request):
        """GET - Show all users"""
        if request.user.is_admin:
            users = Order.objects.all()
        else:
            users = Order.objects.filter(user=request.user)
        if users is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST - Add new user"""
        # address_id = request.data.get("address")

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):
        """GET - Show <email> user"""
        serializer = self.serializer_class(Order.objects.get(id=id))
        return Response(serializer.data)
        # api_result = user_detail.retrieve_the_user(email)
        # return Response(api_result)

