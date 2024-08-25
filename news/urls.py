from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsView, CommentView

router = DefaultRouter()
router.register(r'news', NewsView)
router.register(r'comment', CommentView)

urlpatterns = [
    path('', include(router.urls))
]