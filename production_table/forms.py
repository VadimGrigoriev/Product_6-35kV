from django import forms
from .models import Production


class MyForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ["id", "order_number", "shipment_date", "terminal_series", "serial_number"]
