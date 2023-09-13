from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


def home(request):
    context = {
        'title': 'Домашняя страница'
    }
    return render(request, 'catalog/home.html', context=context)


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'



def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
