from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import serializers, status

from drf_yasg.utils import swagger_auto_schema


class TokenObtainSerrializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainSerrializer,
        }
    )
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


class TokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(method="post")
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


class TokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(method="post")
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
