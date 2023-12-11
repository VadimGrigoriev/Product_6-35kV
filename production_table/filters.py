import django_filters

from production_table.models import Production


class ProductionFilter(django_filters.FilterSet):
    class Meta:
        model = Production

