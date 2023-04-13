from rest_framework import authentication
from main_menu.models import Menu
from .serializers import MenuSerializer
from rest_framework import viewsets

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Menu.objects.all()