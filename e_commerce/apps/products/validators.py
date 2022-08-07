from django.db.utils import IntegrityError

from e_commerce.apps.users.models import User

from rest_framework import serializers
from .models import Product


class IsUniqueWithPublisher:
    message = "The following values should be unique with 'published_by': %s"
    requires_context = True

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value, serializer):
        user = User.objects.get(id=serializer.context["request"].user.id)
        model = serializer.Meta.model

        data = {}
        for field_name in self.fields:
            data[field_name] = value.get(field_name)
        
        query = model.objects.filter(**{**data, "published_by": user})
        if query.exists():
            raise serializers.ValidationError(
                    self.message % ", ".join(self.fields)
                )