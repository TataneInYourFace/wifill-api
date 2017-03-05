from rest_framework import viewsets, status
from rest_framework.response import Response

from app.permissions.user_permission import *
from app.serializers import UserSerializer
from app.models import User
from rest_framework_jwt.settings import api_settings


class UserViewSet(viewsets.ViewSet):

    permission_classes = (IsPostOrIsAuthenticated, IsOwnerOrIsAdmin,)
    serializer_class = UserSerializer
    # Router class variables
    lookup_field = 'email'
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,8}'

    def list(self, request):
        """GET - Show all users"""
        if request.user.is_admin:
            users = User.objects.all()
        else:
            users = User.objects.filter(email=request.user.email)
        if users is None:
            return Response({})
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST - Add new user"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = serializer.data.copy()
            response.update({'token': token})
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, email=None):
        user = User.objects.get(email=email)
        self.check_object_permissions(request, user)
        if not self.request.user.is_admin and "is_admin" in request.data:
            request.data.pop("is_admin")
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, email=None):
        """GET - Show <email> user"""
        serializer = self.serializer_class(User.objects.get(email=email))
        return Response(serializer.data)
        # api_result = user_detail.retrieve_the_user(email)
        # return Response(api_result)

    def partial_update(self, request, email=None):
        return Response()

    def destroy(self, request, email=None):
        """DETELE - Delete <email> user"""
        # api_result = user_detail.destroy_the_user(email)
        # return Response(api_result)

    def can_write(self, request, email=None):
        if email is None and request.data['email']:
            return request.user.is_admin or request.user.email == request.data['email']
        elif email is None:
            return request.user.is_admin
        else:
            return request.user.is_admin or request.user.email == email
