"""
Serializers for converting json data to python objects from and forth

a few notes:
- Django's design principles don't necessarily state that everything has to be this coupled as in,
multiple serializers placed on the same file (same with models/views),
but it's so common as to be sort of an "industry standard";
- see: https://docs.djangoproject.com/en/2.2/misc/design-philosophies/
"""

from rest_framework import serializers

from profitweb.core.models import Client, Product, OrderItem, Order


class ClientSerializer(serializers.ModelSerializer):
    # NOTE: id exposure has to be explicit
    id = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate(self, data):
        """
        validations for the order item object
        """
        # NOTE: validations that can't or shouldn't be placed on db gets attached to the serialization process

        # checks if quantity is divisible by multiplier (or null valued)
        multiplier = data['product']['multiplier']
        if (multiplier is not None) and (data['quantity'] % multiplier != 0):
            raise serializers.ValidationError("Product quantity must be divisible by %s." % multiplier)

        # checks bad profitability (item price is less than 90% of product's cost)
        product_price = data['product']['unit_price']
        item_price = data['unit_price']
        if item_price < (0.9*product_price):
            raise serializers.ValidationError("Item price can't have bad profit margin.")

        # pass
        return data
