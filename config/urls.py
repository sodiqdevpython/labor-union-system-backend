
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Labor union system API",
      default_version='v1',
      description="Labor union system by Alfraganus university students",
      terms_of_service="sodiqdev.netlify.app",
      contact=openapi.Contact(email="sodiqdevpython@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('dj_rest_auth.urls')),
   path('auth/register/', include('dj_rest_auth.registration.urls')),

   # apps
   path('application/', include('applications.urls')),
   path('', include('employee.urls')),
   path('news/', include('news.urls')),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)