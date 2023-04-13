from rest_framework import viewsets
from home.models import Ferry,Mndhej,Nhuddi,SubMenu,Zadsfs
from .serializers import FerrySerializer,MndhejSerializer,NhuddiSerializer,SubMenuSerializer,ZadsfsSerializer
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})

class SubMenuViewSet(viewsets.ModelViewSet):
    serializer_class = SubMenuSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = SubMenu.objects.all()

class MndhejViewSet(viewsets.ModelViewSet):
    serializer_class = MndhejSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Mndhej.objects.all()

class ZadsfsViewSet(viewsets.ModelViewSet):
    serializer_class = ZadsfsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Zadsfs.objects.all()

class FerryViewSet(viewsets.ModelViewSet):
    serializer_class = FerrySerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Ferry.objects.all()

class NhuddiViewSet(viewsets.ModelViewSet):
    serializer_class = NhuddiSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Nhuddi.objects.all()
