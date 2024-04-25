from django.urls import path

from .views import CreateUserView, GetUserView, RefreshUserJWTTokenView, SignInUserView

urlpatterns = [
    path("users/my", GetUserView.as_view()),
    path("users/signup", CreateUserView.as_view()),
    path("users/signin", SignInUserView.as_view()),
    path("users/refresh", RefreshUserJWTTokenView.as_view()),
]
