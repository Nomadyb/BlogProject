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


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             username = request.data.get('username')
#             email = request.data.get('email')
#             password = request.data.get('password')
#             role = request.data.get('role')

#             if not (username and email and password):
#                 return Response({
#                     'isSuccess': False,
#                     'message': 'Registration failed',
#                     'errors': {'detail': 'Username, email, and password are required.'}
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
#                 return Response({
#                     'isSuccess': False,
#                     'message': 'Registration failed',
#                     'errors': {'detail': 'Username or email is already taken.'}
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             # Kullanıcı oluştur
#             user = User.objects.create(
#                 username=username,
#                 email=email,
#                 password=make_password(password),
#                 role=role
#             )
#             user.is_active = True
#             user.save()

#             # # JWT ayarlarını al
#             # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#             # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#             # # JWT token oluştur
#             # payload = jwt_payload_handler(user)
#             # token = jwt_encode_handler(payload)

#             # Token objesini kaydet
#             # Token.objects.create(user=user)

#             user_data = {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'role': user.role,
#                 'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
#                 'is_active': user.is_active,
#             }

#             # Log kaydı tutma
#             logger = logging.getLogger(__name__)
#             logger.info(f'New user registered: {user.username}')

#             return Response({
#                 'isSuccess': True,
#                 'message': 'Registration successful',
#                 'data': user_data,
#                 # 'token': token
#             }, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             # Hata durumunda log kaydı tutma
#             logger = logging.getLogger(__name__)
#             logger.error(f'An error occurred during registration: {str(e)}')

#             return Response({
#                 'isSuccess': False,
#                 'message': 'An error occurred during registration',
#                 'error': str(e),
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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



# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')


#         user = authenticate(request, email=email, password=password)
#         #TODO:
#         if user:
#             #data
#             user_data = {
#                 "id":user.id,
#                 "username": user.username,


#             }


#             jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#             jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#             payload = jwt_payload_handler(user)
#         else:

#             token = jwt_encode_handler(payload)

#             return Response({'token': token}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Burada yapılacak işlemleri ekleyin
        return Response({"message": "Welcome to the internet Have a look around"})
