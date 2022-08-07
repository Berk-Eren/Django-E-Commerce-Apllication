from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Order
from e_commerce.apps.products.models import Product
from e_commerce.apps.products.serializers import ProductSerializer


USER_MODEL = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.slug")

    class Meta:
        model = Order
        fields = ["user", "product", "status"]
        read_only_fields = ["user", "status"]

    def create(self, validated_data):
        user = USER_MODEL.objects.get(id=self.context["request"].user.id)
        validated_data["user"] = user
        validated_data["product"] = Product.objects.get(
                                        slug=validated_data["product"]["slug"]
                                    )

        instance = super().create(validated_data)

        return instance
