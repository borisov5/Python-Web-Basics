from django.urls import include, path

from domfix.domfix_products.views import add_product, details_product, edit_product, delete_product

urlpatterns = (
    path('add/', add_product, name='add product'),
    path('<str:username>/product/<slug:product_name>/', include([
        path('', details_product, name='details product'),
        path('edit/', edit_product, name='delete product'),
        path('delete/', delete_product, name='delete product'),
    ]))
)