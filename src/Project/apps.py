from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Project'


class DeliveryConfig(AppConfig):
    name = 'delivery'


class EmpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emp'
