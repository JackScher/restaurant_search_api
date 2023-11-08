from django.urls import path, include
from rest_framework import routers
from .views import DishViewSet


router = routers.SimpleRouter()
router.register("", DishViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
