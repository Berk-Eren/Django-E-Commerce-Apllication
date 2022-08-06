from rest_framework import serializers
from .models import Product, Category, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "tag"]
        read_only_fields = ["published_by", "stock"]
    
    def create(self):
        instance = super().create()

        request = self.context["request"]
        instance.published_by = request.user

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ["name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        read_only_fields = ["name"]
