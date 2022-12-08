from django.shortcuts import render


def add_product(request):
    return render(request, 'products/product-add-page.html')


def details_product(request, username, product_name):
    return render(request, 'products/product-details-page.html')


def edit_product(request, username, product_name):
    return render(request, 'products/product-edit-page.html')


def delete_product(request, username, product_name):
    return render(request, 'products/product-delete-page.html')

