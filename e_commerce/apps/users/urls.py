from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views


router = SimpleRouter(trailing_slash=True)

router.register(r'', views.UserListCreateView, basename='user')
router.register(r'', views.UserDetailUpdateDeleteView, basename='user')

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
