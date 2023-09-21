from django.urls import path

from catalog.views import home, contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete')

]
