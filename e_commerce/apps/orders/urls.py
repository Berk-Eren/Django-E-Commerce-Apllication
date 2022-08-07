from django.urls import path, include
from rest_framework import routers

from . import viewsets


router = routers.SimpleRouter()
router.register("", viewsets.OrderViewSet, basename="order")

urlpatterns = router.urls