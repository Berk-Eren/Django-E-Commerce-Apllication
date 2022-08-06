from rest_framework import serializers
from .models import Product, Category, Tag


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(),
                                    required=False)
    categories = serializers.ListField(child=serializers.CharField(),
                                        required=False)
    class Meta:
        model = Product
        fields = ["name", "price", "categories", "tags"]
        read_only_fields = ["published_by", "stock"]
    
    def create(self, validated_data):
        validated_data["published_by"] = self.context["request"].user
        
        for tag_name in validated_data["tags"]:
            Tag.objects.get_or_create(name=tag_name)

        for category_name in validated_data["categories"]:
            Category.objects.get_or_create(name=category_name)
        
        instance = super().create(validated_data)

        #request = self.context["request"]
        #instance.published_by = request.user

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ["name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        read_only_fields = ["name"]
