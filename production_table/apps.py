from django.apps import AppConfig


class ProductionTableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'production_table'
