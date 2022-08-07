from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter

from . import viewsets
from . import views


router = SimpleRouter()
router.register("", viewsets.ProductViewset, basename="products")

urlpatterns = [
    path("tags/", views.list_of_tags, name="tag-list"),
    path("categories/", views.list_of_categories, name="category-list"),
    path("", include(router.urls)),
]