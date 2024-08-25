from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationView

router = DefaultRouter()
router.register(r'', ApplicationView)

urlpatterns = [
    path('', include(router.urls))
]