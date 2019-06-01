"""profitweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""

from django.urls import path, include
from rest_framework import routers

from profitweb.core.views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'users', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
