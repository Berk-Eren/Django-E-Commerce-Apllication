from .models import Product
from .serializers import ProductSerializer
from e_commerce.core.mixins import RedisCacheMixin

from rest_framework import viewsets, parsers


class ProductViewset(RedisCacheMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, )
