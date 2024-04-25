from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-hd&it%&vju5x%mc_j7m0lhxoa_ziv68o16_kpqo7b37!d6im^p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# * Django Apps
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# * Third-Party Apps
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
]

# * Business Apps
BUSINESS_APPS = [
    "apps.posts.apps.PostsConfig",
    "apps.users.apps.UsersConfig",
]

# * Installed Apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + BUSINESS_APPS

# * Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.routes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.gateway.wsgi.application"


# * DB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test",
        "USER": "postgres",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# * DRF
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# * JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "DRF-spectacular-test!!@@",
    "USER_ID_FIELD": "email",
    "TOKEN_OBTAIN_SERIALIZER": "apps.users.serializers.CustomTokenObtainPairSerializer",
}

# * User Model
AUTH_USER_MODEL = "users.User"

# * Spectacular
# * https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = {
    "TITLE": "DRF Spectacular test",
    "DESCRIPTION": "DRF Spectacular test project",
    "CONTACT": {"name": "JngMkk", "email": "kjm0817ss@gmail.com"},
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # * drf-spectacular 버전 업그레이드 없이도 자신의 원하는 swagger-ui 버전을 사용할 수 있음(default: latest)
    # * swagger-ui 버전 정보: https://www.npmjs.com/package/swagger-ui
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.44.0",
    "SWAGGER_UI_FAVICON_HREF": "//unpkg.com/swagger-ui-dist@3.44.0/favicon-32x32.png",
    # "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",
    # "SWAGGER_UI_FAVICON_HREF": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/favicon-32x32.png",
    # "REDOC_DIST": "https://cdn.jsdelivr.net/npm/redoc@latest",
    # * https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경(특정 API url 공유시 유용)
        "persistAuthorization": True,  # True: SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않음
        "displayOperationId": True,  # True: API의 url id 값 노출. 대체로 DRF API name들과 일치하기 때문에 API 찾을 때 유용
        "filter": True,  # True: Swagger UI에서 'Filter by Tag' 검색이 가능
    },
}


# * Password validation
# * https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# * Internationalization
# * https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# * Static files (CSS, JavaScript, Images)
# * https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "static/"

# * Default primary key field type
# * https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
