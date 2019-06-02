"""
We're not really using django's app paradigm as I used the same namespace everywhere
(a single project can have many apps bundled in)
"""

from django.apps import AppConfig


class PwConfig(AppConfig):
    name = 'pw'
