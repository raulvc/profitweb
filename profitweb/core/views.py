"""
Views to expose models as API endpoints
"""

from rest_framework.viewsets import ModelViewSet

from profitweb.core.models import Client, Product, Order
from profitweb.core.serializers import ClientSerializer, ProductSerializer, OrderSerializer


class ClientViewSet(ModelViewSet):
    """
    Client listing
    """
    # auth specific classes would be listed here

    # OEM manipulation
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer


class ProductViewSet(ModelViewSet):
    """
    Product listing
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    """
    Order listing / create
    """
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
