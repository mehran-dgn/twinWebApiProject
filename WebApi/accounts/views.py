from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers.AccountsSerializer import UserCreateSerializer , LogoutSerializer, UserUpdateSerializer
from .PermissionManagers.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .models import User


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Successfully logged out"},
            status = status.HTTP_204_NO_CONTENT
        )
    
class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return User.objects.prefetch_related("projects").get(id = self.request.user.id)
    
    

