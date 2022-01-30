from django.apps import AppConfig


class SpidersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spiders'


    def ready(self):
        import spiders.signals