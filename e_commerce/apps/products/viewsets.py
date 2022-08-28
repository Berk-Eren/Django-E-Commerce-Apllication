from .models import Product
from .serializers import ProductSerializer

from rest_framework import viewsets, parsers

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

@method_decorator(vary_on_headers("Authorization"), name="dispatch")
@method_decorator(cache_page(settings.CACHE_TTL), name="dispatch")
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, )
