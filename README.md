# drf-spectacular

## drf-spectacular vs drf-yasg

### drf-yasg

- OpenAPI 2.0 지원 (3.0은 지원하지 않음.)
- 많은 개발자가 사용하며 커뮤니티 지원
- 프로젝트가 더 이상 적극적으로 유지 관리되지 않아 향후 버전의 Django 및 DRF와 호환성 문제 발생 가능성 있음

### drf-spectacular

- 최신 버전의 Django 및 DRF와 작동하도록 설계됨 (Django=^2.2, DRF=^3.10)

- OpenAPI 3.0 지원

  - 콜백, 웹훅 및 보다 자세한 스키마 구성 등 지원

- 주기적으로 업데이트 됨

- DRF 내에서 표준 관행을 준수하는 데 더 중점을 두는 경향이 있어 일부 상황에서는 drf-yasg보다 유연성이 낮을 수 있음

- Swagger UI의 버전과 설정값들이 drf-spectacular의 버전에 의존하지 않음

  ```python
  SPECTACULAR_SETTINGS = {
      # * drf-spectacular 버전 업그레이드 없이도 자신의 원하는 swagger-ui 버전을 사용할 수 있음(default: latest)
      # * swagger-ui 버전 정보: https://www.npmjs.com/package/swagger-ui
      "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.44.0",
      "SWAGGER_UI_FAVICON_HREF": "//unpkg.com/swagger-ui-dist@3.44.0/favicon-32x32.png",
      # "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",
      # "SWAGGER_UI_FAVICON_HREF": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/favicon-32x32.png",
      # "REDOC_DIST": "https://cdn.jsdelivr.net/npm/redoc@latest",
    	...
  }
  ```

- Swagger UI 자체에서 제공하는 UI 커스터마이징 옵션들 또한 자유롭게 조절 가능

  ```python
  SPECTACULAR_SETTINGS = {
    	...
      # * https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
      "SWAGGER_UI_SETTINGS": {
          "deepLinking": True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경(특정 API url 공유시 유용)
          "persistAuthorization": True,  # True: SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않음
          "displayOperationId": True,  # True: API의 url id 값 노출. 대체로 DRF API name들과 일치하기 때문에 API 찾을 때 유용
          "filter": True,  # True: Swagger UI에서 'Filter by Tag' 검색이 가능
      },
  }
  ```



## 사용 방법

1. drf-spectacular install

   ```bash
   poetry add drf-spectacular
   pip install drf-spectacular
   ```

2. 앱 등록 및 drf 설정

   ```python
   # settings.py
   ...
   
   # Installed Apps
   INSTALLED_APPS = [
       "rest_framework",
       "drf_spectacular",
   ]
   
   # DRF
   REST_FRAMEWORK = {
       "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
   }
   ```

3. API View 등록

   ```python
   from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
   
   if settings.DEBUG:
       urlpatterns += [
           path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
           path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
           path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
       ]
   ```

4. Custom settings

   - API 인증 방식

   - API 조회 권한 설정

     ```python
     SPECTACULAR_SETTINGS = {
       	...
     		"SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],
       	...
     }
     ```

