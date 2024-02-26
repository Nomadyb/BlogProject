from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model  # Kullanıcı modelini al
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# Create your views here.
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework_jwt.settings import api_settings
import logging

# User = get_user_model()


# TODO: email pasword kontrol et serializer içinde
# TODO kullanıcı var mı yok mu
# TODO: authentication döndürülmeli
# TODO: veritabanında token tutma django jwt token  kullan





from rest_framework.response import Response
from rest_framework import status
import logging


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)

                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
                    'is_active': user.is_active,
                }

                logger = logging.getLogger(__name__)
                logger.info(f'New user registered: {user.username}')

                return Response({
                    'isSuccess': True,
                    'message': 'Registration successful',
                    'data': user_data,
                    'refresh': str(refresh),
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'isSuccess': False,
                    'message': 'Registration failed',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f'An error occurred during registration: {str(e)}')
            return Response({
                'isSuccess': False,
                'message': 'An error occurred during registration',
                'error': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request, email=email, password=password)

            if user:
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
                    'is_active': user.is_active,
                }

                refresh = RefreshToken.for_user(user)

                logger = logging.getLogger(__name__)
                logger.info(f'User logged in: {user.username}')

                return Response({
                    'isSuccess': True,
                    'message': 'Login successful',
                    'data': user_data,
                    'refresh': str(refresh),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f'An error occurred during login: {str(e)}')
            return Response({'error': 'An error occurred during login'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Burada yapılacak işlemleri ekleyin
        return Response({"message": "Welcome to the internet Have a look around"})
