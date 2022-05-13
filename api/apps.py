from django.apps import AppConfig
from django import dispatch

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals