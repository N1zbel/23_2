from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Домашняя страница'
    }
    return render(request, 'catalog/home.html', context)


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


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'title': product
    }
    return render(request, 'catalog/product.html', context=context)
