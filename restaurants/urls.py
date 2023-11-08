from django.urls import path, include
from rest_framework import routers

from .views import RestaurantViewSet


router = routers.SimpleRouter()
router.register("", RestaurantViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
