from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FerryViewSet,MndhejViewSet,NhuddiViewSet,SubMenuViewSet,ZadsfsViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('submenu', SubMenuViewSet )
router.register('mndhej', MndhejViewSet )
router.register('zadsfs', ZadsfsViewSet )
router.register('ferry', FerryViewSet )
router.register('nhuddi', NhuddiViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
