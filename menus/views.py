from rest_framework.viewsets import ModelViewSet
from employees.permissions import IsAdminOrReadOnly

from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]
