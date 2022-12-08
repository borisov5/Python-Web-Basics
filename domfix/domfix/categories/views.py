from django.shortcuts import render


def dry_construction_products(request):
    return render(request, 'categories/dry-construction-products-page.html')


def thermal_insulation_products(request):
    return render(request, 'categories/thermal-insulation-products-page.html')


def water_supply_and_sanitation_products(request):
    return render(request, 'categories/water-supply-and-sanitation-products-page.html')


def construction_chemistry_products(request):
    return render(request, 'categories/construction-chemistry-products-page.html')


def tools_products(request):
    return render(request, 'categories/tools-products-page.html')


def painting_products(request):
    return render(request, 'categories/painting-products-page.html')


