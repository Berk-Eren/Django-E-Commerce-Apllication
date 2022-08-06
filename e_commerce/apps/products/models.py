import random

from django.db import models

from e_commerce.apps.users.models import User
from e_commerce.core.slugify import unique_slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField("Category", related_name="products")
    tags = models.ManyToManyField("Tag", related_name="products")
    stock = models.IntegerField(default=0)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=25, unique=True)

    class Meta:
        unique_together = (('name', 'published_by'), )

    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self.name + self.published_by.username)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=30)
