"""
Views to expose models as API endpoints
"""
from drf_rw_serializers import generics
from rest_framework.viewsets import ModelViewSet

from profitweb.core.models import Client, Product, Order
from profitweb.core.serializers import ClientSerializer, ProductSerializer, OrderCreateSerializer, \
    OrderListSerializer


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


class OrderListCreateView(generics.ListCreateAPIView):
    """
    Order listing / create
    (separate serializers for each operation)
    """
    queryset = Order.objects.all().order_by('id')
    write_serializer_class = OrderCreateSerializer
    read_serializer_class = OrderListSerializer

    # NOTE: To intercept requests I could override these methods:
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
