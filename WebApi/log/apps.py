from django.apps import AppConfig

class LogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'log'

    def ready(self):
        from .signals import article_signals
