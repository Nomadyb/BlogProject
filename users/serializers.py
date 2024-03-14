from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model




User = get_user_model()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=70)
    role = serializers.ChoiceField(
        choices=["ADMIN", "BLOGGER"], default="BLOGGER", required=False
    )

    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        # return User.objects.create(**validated_data)
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.save()
        return instance

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Bu e-posta adresi zaten kullanılıyor.")

        return attrs




    # def validate(self, attrs):
    #     email = attrs.get("email")
    #     password = attrs.get("password")

    #     try:
    #         validate_email(email)
    #     except ValidationError:
    #         raise serializers.ValidationError("Invalid email format")

    #     try:
    #         validate_password(password)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e.messages)

    #     return attrs




# class IdSerializer(serializers.Serializer):
#     id = serializers.IntegerField()

#     # def validate(self,attrs):
#     #     return attrs



# class CreateUserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=70)
#     role = serializers.ChoiceField(
#         choices=["ADMIN", "BLOGGER"], default="BLOGGER")
#     password = serializers.CharField(max_length=128, write_only=True)

#     def create(self, validated_data):
#         # return User.objects.create(**validated_data)
#         user = User.objects.create_user(**validated_data)
#         return user

#     def validate(self, attrs):
#         #TODO: yukarıdaki fieldlardan kullan. 
#         email = attrs.get("email")
#         password = attrs.get("password")

#         try:
#             validate_email(email)
#         except ValidationError:
#             raise serializers.ValidationError("Invalid email format")

#         try:
#             validate_password(password)
#         except ValidationError as e:
#             raise serializers.ValidationError(e.messages)

#         return attrs


# class UpdateUserSerializer(IdSerializer):
#     username = serializers.CharField(max_length=100, required=False)
#     email = serializers.EmailField(max_length=70, required=False)
#     role = serializers.ChoiceField(
#         choices=["ADMIN", "BLOGGER"], default="BLOGGER", required=False)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get("username", instance.username)
#         instance.email = validated_data.get("email", instance.email)
#         instance.role = validated_data.get("role", instance.role)
#         instance.save()
#         return instance

