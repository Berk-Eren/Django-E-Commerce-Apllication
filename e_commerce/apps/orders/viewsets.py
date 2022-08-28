from rest_framework import viewsets, permissions

from .models import Order
from .serializers import OrderSerializer

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


@method_decorator(vary_on_headers("Authorization"), name="dispatch")
@method_decorator(cache_page(settings.CACHE_TTL), name="dispatch")
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
