from rest_framework.viewsets import ModelViewSet
from employees.permissions import IsAdminOrReadOnly

from .models import Dish
from .serializers import DishSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]
