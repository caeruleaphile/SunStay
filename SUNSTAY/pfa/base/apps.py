from django.apps import AppConfig

class SunStayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    verbose_name = 'SunStay'

    def ready(self):
         pass
