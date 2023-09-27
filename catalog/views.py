from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    context = {
        'title': 'Домашняя страница'
    }
    return render(request, 'catalog/home.html', context=context)


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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        form.instance.author = self.request.user

        selected_version = form.cleaned_data['version']
        product = form.save(commit=False)
        product.save()
        product.versions.set([selected_version])
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        form.instance.author = self.request.user

        selected_version = form.cleaned_data['version']
        product = form.instance
        product.versions.clear()
        product.versions.add(selected_version)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products')

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.author == self.request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())

        return HttpResponseForbidden("Вы не можете удалить этот товар")
