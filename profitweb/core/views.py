from rest_framework import viewsets

from profitweb.core.models import Client
from profitweb.core.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    Client endpoint
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
