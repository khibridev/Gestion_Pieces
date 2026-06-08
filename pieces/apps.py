from django.apps import AppConfig

class PiecesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pieces'

    def ready(self):
        import pieces.signals