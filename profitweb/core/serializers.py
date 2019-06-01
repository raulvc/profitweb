"""
Serializers for converting json data to python objects from and forth
"""

from rest_framework import serializers

from profitweb.core.models import Client, Product, OrderItem, Order


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    # NOTE: id exposure has to be explicit
    id = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate(self, data):
        """
        performs order item validation (after serializing, before model conversion)
        """
        # returns true if quantity is divisible by multiplier or multiplier is null valued
        multiplier = data['product']['multiplier']
        if (multiplier is None) or (data['quantity'] % multiplier == 0):
            return data
        raise serializers.ValidationError("Product quantity must be divisible by %s." % multiplier)
