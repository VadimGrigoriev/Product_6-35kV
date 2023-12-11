import django_tables2 as tables

from production_table.models import Production


class ProductionTable(tables.Table):

    class Meta:
        model = Production
