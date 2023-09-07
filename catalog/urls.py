import products as products
from django.urls import path

from catalog.views import home, contacts, detail_product

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('product/<pk>', detail_product)
]