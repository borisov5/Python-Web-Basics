from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('domfix.common.urls')),
    path('accounts/', include('domfix.accounts.urls')),
    path('partners/', include('domfix.partners.urls')),
    path('products/', include('domfix.domfix_products.urls')),
    path('products/', include('domfix.categories.urls')),
]
