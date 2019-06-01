"""
Views to expose models as API endpoints
"""

from rest_framework import viewsets

from profitweb.core.models import Client, Product
from profitweb.core.serializers import ClientSerializer, ProductSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    Client listing
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product listing
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
