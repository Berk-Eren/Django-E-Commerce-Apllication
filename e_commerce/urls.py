"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from e_commerce.core.views import AuthTokenView

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView
)
from e_commerce.core.serializers import TokenObtainPairView as CustomTokenObtainPairView


schema_view = get_schema_view(
   openapi.Info(
      title="E Commerce API",
      default_version='v1',
      description="This is the Swagger documentation of the simple E-Commerce project.",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("e_commerce.apps.users.urls")),
    path('orders/', include("e_commerce.apps.orders.urls")),
    path('products/', include("e_commerce.apps.products.urls")),

    path('obtain_token/', AuthTokenView.as_view(), name="obtain-token"),

    path('jwt_token/', TokenObtainPairView.as_view(), name="obtain-jwt-token"),
    path('custom_jwt_token/', CustomTokenObtainPairView.as_view(), name="obtain-jwt-token"),
    path('jwt_token/refresh/', TokenRefreshView.as_view(), name="refresh-jwt-token"),
    path('jwt_token/verify/', TokenVerifyView.as_view(), name="verify-jwt-token"),

    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
