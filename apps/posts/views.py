from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .schemas import CREATE_POST_BODY_EX, LIST_POST_PARAMS
from .serializers import PostSerializer


@extend_schema(tags=["posts"])
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @extend_schema(examples=[CREATE_POST_BODY_EX])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(parameters=LIST_POST_PARAMS)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
