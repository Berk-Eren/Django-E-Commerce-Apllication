from django.db import models

from e_commerce.apps.users.models import User
from e_commerce.apps.products.models import Product


class Order(models.Model):
    class Status(models.IntegerChoices):
        ORDERED = 0
        IN_SHIPMENT = 1
        ARRIVED = 2
        CANCELLED = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=Status.choices, 
                                                default=0)
