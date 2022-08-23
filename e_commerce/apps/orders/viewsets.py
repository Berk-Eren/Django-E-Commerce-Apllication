from rest_framework import viewsets, permissions

from .models import Order
from .serializers import OrderSerializer
from e_commerce.core.mixins import RedisCacheMixin


class OrderViewSet(RedisCacheMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
