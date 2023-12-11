from django.urls import path

from .views import create, delete, list_products

urlpatterns = [
    path('', list_products, name='list_products'),
    path('create/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
]
