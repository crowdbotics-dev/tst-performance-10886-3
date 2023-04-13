
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MenuViewSet
router = DefaultRouter()
router.register('menu', MenuViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
