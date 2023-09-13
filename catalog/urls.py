from django.urls import path

from catalog.views import home, contacts, page_not_found, CatalogListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<pk>', ProductDetailView.as_view(), name='product_number'),
    path('catalog/', CatalogListView.as_view(), name='catalog')

]