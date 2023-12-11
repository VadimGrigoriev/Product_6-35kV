from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from production_table.models import Production
from production_table.tables import ProductionTable


def list_products(request):
    terminal_series = Production.objects.all()
    table = ProductionTable(terminal_series)
    return render(request, 'list_products.html', {'list_products': table})


def create(request):
    if request.method == "POST":
        product = Production()
        product.order_number = request.POST.get("order_number")
        product.shipment_date = request.POST.get("shipment_date")
        product.terminal_series = request.POST.get("terminal_series")
        product.serial_number = request.POST.get("serial_number")
        product.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'create_product.html')


def delete(request, id):
    try:
        product = Production.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Production.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
