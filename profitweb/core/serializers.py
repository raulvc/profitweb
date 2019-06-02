"""
Serializers for converting json data to python objects from and forth

a few notes:
- Django's design principles don't necessarily state that everything has to be this coupled as in,
multiple serializers placed on the same file (same with models/views),
but it's so common as to be sort of an "industry standard";
- see: https://docs.djangoproject.com/en/2.2/misc/design-philosophies/
"""
from decimal import Decimal

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


# ============================================================================
# Order create
# ============================================================================
class OrderItemCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=False, queryset=Product.objects.all(),
                                                 error_messages={'does_not_exist': 'Invalid product id'})

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'unit_price')

    def validate(self, data):
        """
        validations for the order item object
        """
        # NOTE: validations that can't or shouldn't be placed on db gets attached to the serialization process

        # checks if quantity is divisible by multiplier (or null valued)
        product = data['product']
        multiplier = product.multiplier
        if (multiplier is not None) and (data['quantity'] % multiplier != 0):
            raise serializers.ValidationError("Product quantity must be divisible by %s." % multiplier)

        # checks bad profitability (item price is less than 90% of product's cost)
        item_price = data['unit_price']
        if item_price < (Decimal(0.9) * product.unit_price):
            raise serializers.ValidationError("Item price can't have bad profit margin.")

        # pass
        return data


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    We need a different serializer for creating orders as we specify relations by id
    """
    items = OrderItemCreateSerializer(many=True)
    client = serializers.PrimaryKeyRelatedField(many=False, queryset=Client.objects.all(),
                                                error_messages={'does_not_exist': 'Invalid client id'})

    class Meta:
        model = Order
        fields = ('client', 'items')

    def create(self, validated_data):
        # unwrapping data from request
        # already serialized and validated, just applying an insertion precedence
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order


# ============================================================================
# Order list
# ============================================================================
class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    total_price = serializers.ReadOnlyField()
    items = OrderItemListSerializer(many=True)
    client = ClientSerializer()

    class Meta:
        model = Order
        fields = ('id', 'client', 'items', 'total_price')
