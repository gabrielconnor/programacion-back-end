from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
# core/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate

def crear_grupos_callback(sender, **kwargs):
    from django.contrib.auth.models import Group
    for rol in ['admin', 'normal', 'viewer']:
        Group.objects.get_or_create(name=rol)

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(crear_grupos_callback, sender=self)