from django.urls import path, include
from rest_framework import routers
from .views import MenuViewSet


router = routers.SimpleRouter()
router.register("", MenuViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
