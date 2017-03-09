from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from app.serializers import UserSerializer
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
import json


class LoginView(APIView):
    """
    Register a new user.
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user and user.is_valide:
            serializer = self.serializer_class(user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = serializer.data.copy()
            response.update({'token': token})
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"non_field_errors": ["Unable to login with provided credentials."]}
            return Response({'errors': response}, status=status.HTTP_400_BAD_REQUEST)
