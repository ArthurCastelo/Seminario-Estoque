from django.apps import AppConfig


def ready(self):
    import core.signals

