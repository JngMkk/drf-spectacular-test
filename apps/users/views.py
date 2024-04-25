from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.auth.token import get_payload

from .models import User
from .serializers import CreateUserSerializer, GetUserSerializer


@extend_schema_view(
    get=extend_schema(
        operation_id="user_profile",
        summary="유저 프로필",
        description="본인 정보 확인!!!!!!!!!!",
        tags=["users"],
    )
)
class GetUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer

    def get_object(self):
        payload = get_payload(self.request)
        self.kwargs["pk"] = payload["id"]
        return super().get_object()


@extend_schema_view(
    post=extend_schema(operation_id="user_signup", summary="회원가입", tags=["users"])
)
class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = CreateUserSerializer


@extend_schema_view(
    post=extend_schema(operation_id="user_signin", summary="로그인", tags=["users"])
)
class SignInUserView(TokenObtainPairView):
    permission_classes = [AllowAny]
    authentication_classes = []


@extend_schema_view(
    post=extend_schema(operation_id="user_refresh_token", summary="토큰 refresh", tags=["users"])
)
class RefreshUserJWTTokenView(TokenRefreshView):
    pass
