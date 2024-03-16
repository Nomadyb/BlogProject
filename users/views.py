# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import get_user_model  # Kullanıcı modelini al
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import render

# # Create your views here.
# import logging
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import UserSerializer
# # from rest_framework_jwt.settings import api_settings

# # User = get_user_model()





# from rest_framework.response import Response
# from rest_framework import status
# import logging


# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid():
#                 user = serializer.save()
#                 refresh = RefreshToken.for_user(user)

#                 user_data = {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email,
#                     "role": user.role,
#                     "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
#                     "is_active": user.is_active,
#                 }

#                 logger = logging.getLogger(__name__)
#                 logger.info(f"New user registered: {user.username}")

#                 return Response(
#                     {
#                         "isSuccess": True,
#                         "message": "Registration successful",
#                         "data": user_data,
#                         "refresh": str(refresh),
#                     },
#                     status=status.HTTP_201_CREATED,
#                 )
#             else:
#                 return Response(
#                     {
#                         "isSuccess": False,
#                         "message": "Registration failed",
#                         "errors": serializer.errors,
#                     },
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#         except Exception as e:
#             #TODO: ayrı bir except.py için setting altına bir adet aç modifiye et  
#             logger = logging.getLogger(__name__)
#             logger.error(f"An error occurred during registration: {str(e)}")
#             return Response(
#                 {
#                     "isSuccess": False,
#                     "message": "An error occurred during registration",
#                     "error": str(e),
#                 },
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             email = request.data.get("email")
#             password = request.data.get("password")
#             #TODO: validate ile kontrol et email yapısını 
#             user = authenticate(request, email=email, password=password)

#             if user:
#                 user_data = {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email,
#                     "role": user.role,
#                     "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
#                     "is_active": user.is_active,
#                 }

#                 refresh = RefreshToken.for_user(user)

#                 logger = logging.getLogger(__name__)
#                 logger.info(f"User logged in: {user.username}")

#                 return Response(
#                     {
#                         "isSuccess": True,
#                         "message": "Login successful",
#                         "data": user_data,
#                         "refresh": str(refresh),
#                         "acces": str(refresh.access_token)
#                     },
#                     status=status.HTTP_200_OK,
#                 )
#             else:
#                 return Response(
#                     {"error": "Invalid credentials"},
#                     status=status.HTTP_401_UNAUTHORIZED,
#                 )
#         except Exception as e:
#             logger = logging.getLogger(__name__)
#             logger.error(f"An error occurred during login: {str(e)}")
#             return Response(
#                 {"error": "An error occurred during login"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
# #TODO: json dosyadan key geldiğinde hata olan satırı döndür chatgpt ile dene



# class HomeView(APIView):
#     permission_classes = [IsAuthenticated]
#     #TODO: jwt authentication için bir satırlık 


#     def get(self, request):
#         return Response({"message": "Welcome to the internet Have a look around"})


# views.py


"""
custom_exception_handler.py dosyası kullanmadan 
"""

# from rest_framework.response import Response
# from rest_framework import status
# import logging
# from rest_framework.views import APIView
# from .serializers import CreateUserSerializer, IdSerializer, UpdateUserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from django.contrib.auth import authenticate
# from django.shortcuts import render


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             serializer = CreateUserSerializer(data=request.data)
#             if serializer.is_valid():
#                 user = serializer.save()
#                 refresh = RefreshToken.for_user(user)

#                 user_data = {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email,
#                     "role": user.role,
#                     "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
#                     "is_active": user.is_active,
#                 }

#                 logger = logging.getLogger(__name__)
#                 logger.info(f"New user registered: {user.username}")

#                 return Response(
#                     {
#                         "isSuccess": True,
#                         "message": "Registration successful",
#                         "data": user_data,
#                         "refresh": str(refresh),
#                     },
#                     status=status.HTTP_201_CREATED,
#                 )
#             else:
#                 return Response(
#                     {
#                         "isSuccess": False,
#                         "message": "Registration failed",
#                         "errors": serializer.errors,
#                     },
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#         #TODO: ayrı bir except.py için setting altına bir adet aç modifiye et
#         except Exception as e:
#             logger = logging.getLogger(__name__)
#             logger.error(f"An error occurred during registration: {str(e)}")
#             return Response(
#                 {
#                     "isSuccess": False,
#                     "message": "An error occurred during registration",
#                     "error": str(e),
#                 },
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             email = request.data.get("email")
#             password = request.data.get("password")
#             user = authenticate(request, email=email, password=password)

#             if user:
#                 user_data = {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email,
#                     "role": user.role,
#                     "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
#                     "is_active": user.is_active,
#                 }

#                 refresh = RefreshToken.for_user(user)

#                 logger = logging.getLogger(__name__)
#                 logger.info(f"User logged in: {user.username}")

#                 return Response(
#                     {
#                         "isSuccess": True,
#                         "message": "Login successful",
#                         "data": user_data,
#                         "refresh": str(refresh),
#                         "access": str(refresh.access_token)
#                     },
#                     status=status.HTTP_200_OK,
#                 )
#             else:
#                 return Response(
#                     {"error": "Invalid credentials"},
#                     status=status.HTTP_401_UNAUTHORIZED,
#                 )
#         except Exception as e:
#             logger = logging.getLogger(__name__)
#             logger.error(f"An error occurred during login: {str(e)}")
#             return Response(
#                 {"error": "An error occurred during login"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )


# class HomeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "Welcome to the internet. Have a look around."})


import json
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import CreateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = CreateUserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)

                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_active": user.is_active,
                }

                logger = logging.getLogger(__name__)
                logger.info(f"New user registered: {user.username}")
                
                # JSON dosyasından 'key' alındığında hata oluştur
                key = request.data.get('key')
                if key:
                    raise ValueError("Invalid key received")

                return Response(
                    {
                        "isSuccess": True,
                        "message": "Registration successful",
                        "data": user_data,
                        "refresh": str(refresh),
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "isSuccess": False,
                        "message": "Registration failed",
                        "errors": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return custom_exception_handler(e, __name__)
            # #TODO: json dosyadan key geldiğinde hata olan satırı döndür chatgpt ile dene




class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            user = authenticate(request, email=email, password=password)

            if user:
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_active": user.is_active,
                }

                refresh = RefreshToken.for_user(user)

                logger = logging.getLogger(__name__)
                logger.info(f"User logged in: {user.username}")

                return Response(
                    {
                        "isSuccess": True,
                        "message": "Login successful",
                        "data": user_data,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        except Exception as e:
            return custom_exception_handler(e, __name__)  


# class HomeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             return Response({"message": "Welcome to the internet. Have a look around."})
#         except Exception as e:
#             return custom_exception_handler(e, __name__)





class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

#TODO: blog için kullanıcının kendi değerlerini al db'den tüm satırı seç yada kullanıcıya özgü olmalı
# TODO: admin için ise tüm kullanıcılar listelenmeli 
class HomeView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        try:
            return Response(
                {
                    "isSuccess": True,
                    "message": "Login successful",
                    "data": request.user.username,

                },
                status=status.HTTP_200_OK,
            )
 

        except Exception as e:
            return custom_exception_handler(e, __name__) 

    # User = get_user_model()
    # serializer_class = UserSerializer
    # queryset = User.objects.all()
    # pagination_class = StandardResultsSetPagination



