import csv
from django.core.management.base import BaseCommand

from production_table.models import TerminalSeries


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('terminal_series.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = list(csv.DictReader(csv_file, delimiter=';'))
            for row in csv_reader:
                TerminalSeries.objects.create(
                    id=int(row['id']),
                    terminal_series=row['terminal_series'],
                    description=row['description']
                )