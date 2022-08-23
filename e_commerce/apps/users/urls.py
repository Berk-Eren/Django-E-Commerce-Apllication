from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from . import viewsets


router = SimpleRouter(trailing_slash=True)

router.register(r'', viewsets.UserListCreateView, basename='user')
router.register(r'', viewsets.UserDetailUpdateDeleteView, basename='user')

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
