from rest_framework import serializers

from .models import Product, Category, Tag
from .validators import IsUniqueWithPublisher

from e_commerce.apps.users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        read_only_fields = ["name"]

    def to_representation(self, instance):
        return instance.name


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

    def to_representation(self, instance):
        return instance.name


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.ListSerializer(child=serializers.CharField())
    categories = serializers.ListSerializer(child=serializers.CharField())
    published_by = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ["name", "price", "categories", "tags", "published_by", 
                    "stock", "image"]
        read_only_fields = ["published_by", "stock"]
        validators = [
            IsUniqueWithPublisher(
                fields = ["name"]
            )
        ]
    
    def create(self, validated_data):
        auth_user = User.objects.get(id=self.context["request"].user.id)
        validated_data["published_by"] = auth_user
        
        tags = validated_data.pop("tags", [])
        categories = validated_data.pop("categories", [])
        
        instance = super().create(validated_data)

        for tag_name in tags:
            inst, _ = Tag.objects.get_or_create(name=tag_name)
            inst.products.add(instance.id)

        for category_name in categories:
            inst, _ = Category.objects.get_or_create(name=category_name)
            inst.products.add(instance.id)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = instance.slug
        
        return {slug: representation}
