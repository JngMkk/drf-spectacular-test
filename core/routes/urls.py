from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("api/", include("apps.posts.urls")),
    path("api/", include("apps.users.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
