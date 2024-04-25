from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, ModelSerializer, ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class GetUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_admin")


class CreateUserSerializer(ModelSerializer):
    password = CharField(write_only=True, validators=[validate_password])
    password2 = CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError("Password fields didn't match.")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(validated_data["email"], validated_data["password"])


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["id"] = user.id
        token["is_admin"] = user.is_admin
        return token
