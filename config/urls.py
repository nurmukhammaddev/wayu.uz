from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from config.settings import DEBUG
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Wayu API Docs",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mashrapov3030@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair',),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('about/', include('apps.about.urls'), name='about'),
    path('blog/', include('apps.blog.urls'), name='blog'),
    path('contact/', include('apps.contact.urls'), name='contact'),
    path('home/', include('apps.home.urls'), name='home'),
    path('portfolio/', include('apps.portfolio.urls'), name='portfolio'),
    path('services/', include('apps.service.urls'), name='services'),

]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
