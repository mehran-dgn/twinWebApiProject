from rest_framework import serializers
from ..models import User, UserProjects
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name"
            #"dashboard_link"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        token = RefreshToken(self.validated_data["refresh"])
        token.blacklist()


class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjects
        fields = ["title", "description", "project_url"]


class UserUpdateSerializer(serializers.ModelSerializer):
    projects = UserProjectSerializer(many=True, read_only = True)

    class Meta:
        model = User 
        fields = [
             "first_name",
            "last_name",
            "mobile_phone",
            "company_phone",
            "postal_code",
            "address",
            "projects"
        ]

        read_only_fields = ["projects"]