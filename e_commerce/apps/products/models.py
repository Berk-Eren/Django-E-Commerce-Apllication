import random

from django.db import models
from django.utils.text import slugify

from e_commerce.apps.users.models import User
from e_commerce.core.utils import unique_slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField("Category", related_name="products")
    tags = models.ManyToManyField("Tag", related_name="products")
    stock = models.IntegerField(default=0)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="photos/",
                                default="photos/default_product.jpg")

    class Meta:
        unique_together = (('name', 'published_by_id'), )

    def save(self, *args, **kwargs):
        slug = slugify(self.name + " " + self.published_by.username)
        self.slug = slug + "-" + unique_slugify(slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s published by %s (%s)" % (self.name,
                                                self.published_by.username,
                                                    self.slug)

    """@property
    def get_published_by_id(self):
        return self.published_by.id
    """


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
