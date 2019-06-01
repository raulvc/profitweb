"""
Modeling
"""

# NOTE: there's no separation between domain logic and model declaration in django

from decimal import Decimal

from django.db import models
from rest_framework.compat import MinValueValidator


class Client(models.Model):
    name = models.TextField(
        null=False,
        blank=False
    )


class Product(models.Model):
    name = models.TextField(
        null=False,
        blank=False
    )
    unit_price = models.DecimalField(
        null=False,
        decimal_places=2,
        max_digits=12,

        # NOTE: in validator context a decimal object must be declared (0.01 can't be inferred)
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    multiplier = models.PositiveIntegerField(
        null=True
    )


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING,
        null=False
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        # NOTE: naming a relation makes it easier to reference on a parent object
        Order, related_name="items", on_delete=models.DO_NOTHING,
        null=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING,
        null=False
    )
    quantity = models.PositiveIntegerField(
        null=False,
        validators=[MinValueValidator(1)]
    )
    unit_price = models.DecimalField(
        null=False,
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(Decimal('0.01'))]
    )

    def description(self):
        # just a shortcut for displaying product's name
        return self.product.name
