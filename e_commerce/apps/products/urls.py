from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter

from . import viewsets


router = SimpleRouter()
router.register("", viewsets.ProductViewset, basename="products")

urlpatterns = [
    path("", include(router.urls))
]