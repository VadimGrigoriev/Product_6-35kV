from django.db import models


class SerialNumber(models.Model):
    """Серийные номера"""
    serial_number = models.IntegerField(unique=True, verbose_name='Номер терминала')


class TerminalSeries(models.Model):
    """Серия терминала"""
    terminal_series = models.CharField(max_length=10, unique=True, verbose_name='Серия терминала')
    description = models.TextField(verbose_name='Описание')


class Production(models.Model):
    """Продукция 6-35кВ"""
    order_number = models.IntegerField(verbose_name='Номер заказа')
    shipment_date = models.DateField(verbose_name='Дата отгрузки')
    terminal_series = models.CharField(max_length=10, verbose_name='Серия терминала')
    serial_number = models.IntegerField(unique=True, verbose_name='Номер терминала')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # client = models.TextField(blank=True, null=True, verbose_name='Заказчик')
    # odject = models.TextField(blank=True, null=True, verbose_name='Объект')
    # order_date = models.DateField(verbose_name='Дата заказа', )
    # terminal_series = models.ForeignKey(
    #     TerminalSeries,
    #     on_delete=models.CASCADE,
    #     verbose_name='Серия терминала')
    # modification = models.CharField(
    #     max_length=5,
    #     blank=True,
    #     null=True,
    #     verbose_name='Модификация')
    # serial_number = models.ForeignKey(
    #     SerialNumber,
    #     on_delete=models.CASCADE,
    #     verbose_name='Номер терминала')
    # description = models.TextField(blank=True, null=True, verbose_name='Описание')
