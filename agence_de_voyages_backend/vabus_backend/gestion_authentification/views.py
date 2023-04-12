from .models import *
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model
from rest_framework.generics import RetrieveAPIView
# import utils.response_handler as rh
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

UserModel = get_user_model()
class RegistrationView(APIView):

    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)
    
class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({'email': ['Invalid email or password.']}, status=status.HTTP_400_BAD_REQUEST)
        response_data = {
            'id': user.id,
            # 'phone_number': user.phone_number,
            'email': user.email,
            # 'email': user.email
        }
        return Response(response_data)

