from django.shortcuts import render

from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from drf_yasg.utils import swagger_auto_schema

from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


@swagger_auto_schema(method="get",
                        operation_description="Get list of categories")
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@vary_on_headers("Authorization")
@cache_page(settings.CACHE_TTL)
def list_of_categories(*args, **kwargs):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method="get",
                        operation_description="Get list of tags")
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@vary_on_headers("Authorization")
@cache_page(settings.CACHE_TTL)
def list_of_tags(*args, **kwargs):
    queryset = Tag.objects.all()
    serializer = TagSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
