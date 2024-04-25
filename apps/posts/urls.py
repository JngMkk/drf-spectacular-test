from django.urls import path

from .views import PostViewSet

urlpatterns = [
    path("posts", PostViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "posts/<int:pk>",
        PostViewSet.as_view({"delete": "destroy", "put": "update", "get": "retrieve"}),
    ),
]
