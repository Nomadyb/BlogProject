from rest_framework import serializers
from .models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import re 


# yapılacak işlemler
"""
burada rest içinde model serializer oluşturuldu
amaç rest api üzerinden kullanıcı bilgilerini almak ve kaydetmek(JSON formatında)

"""
# TODO: meta yapısını kullanmamalısın manuel ekle
# TODO: veriler doğrul
# TODO: role yapısını charfield olarak alma



# class UserSerializer(serializers.Serializer):
#     # permission_classes = (AllowAny,)
#     # def __init__(self,id,username,email,role):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=70)
#     role = serializers.CharField(max_length=100)

#     # verilerin doğrulanmasına bağlı olarak nesnelerin döndürülmesi için hem create hem update uygulanmalıdır
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.role = validated_data.get('role', instance.role)
#         instance.save()
#         return instance

#     # bir validate yazmalısın




# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=100, required=False)
#     email = serializers.EmailField(max_length=70)
#     role = serializers.CharField(max_length=100, required=False)

#     password = serializers.CharField(
#         max_length=128, write_only=True)  # Yeni eklenen password alanı

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.role = validated_data.get('role', instance.role)
#         instance.save()
#         return instance

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if not email:
#             raise serializers.ValidationError(
#                 {'email': 'This field is required.'})
#         if not password:
#             raise serializers.ValidationError(
#                 {'password': 'This field is required.'})

#         return attrs


from rest_framework import serializers
import re
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=70)
    role = serializers.ChoiceField(choices=["ADMIN", "BLOGGER"], default="BLOGGER",required=False)

    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        # return User.objects.create(**validated_data)
        user = User.objects.create_user(**validated_data)
        return user 

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # E-posta formatını kontrol et
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        if not re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            raise serializers.ValidationError("Invalid email format")

        return attrs



# import re




#     def validate_email(self, value):
#         # E-posta formatını kontrol et
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
#             raise serializers.ValidationError("Invalid email format")
#         return value

