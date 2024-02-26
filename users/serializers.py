from rest_framework import serializers
from .models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
import re 


# yapılacak işlemler
"""
burada rest içinde model serializer oluşturuldu
amaç rest api üzerinden kullanıcı bilgilerini almak ve kaydetmek(JSON formatında)

"""
# TODO: meta yapısını kullanmamalısın manuel ekle
# TODO: veriler doğrul
# TODO: role yapısını charfield olarak alma



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

        #re
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        if not re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            raise serializers.ValidationError("Invalid email format")


        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=])[a-zA-Z0-9!@#$%^&*()-_+=]{8,}$", password):
            raise serializers.ValidationError("Invalid password format")
            
        return attrs








