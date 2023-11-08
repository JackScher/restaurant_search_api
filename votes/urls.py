from django.urls import path, include
from rest_framework import routers
from .views import VoteViewSet


router = routers.SimpleRouter()
router.register("", VoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
