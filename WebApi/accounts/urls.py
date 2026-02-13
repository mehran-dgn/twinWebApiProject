from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from . import views 

urlpatterns = [
    path("login/",TokenObtainPairView.as_view(), name = "login"),
    path("refresh/", TokenRefreshView.as_view() , name = "token_refresh"),
    # path("create-user/", views.UserCreateView.as_view()),
    path("logout/",views.LogoutView.as_view() , name="logout" ),
    path("profile/",views.UserProfileView.as_view(), name="profile")
]