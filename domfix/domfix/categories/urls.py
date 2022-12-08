from django.urls import path

from domfix.categories.views import dry_construction_products, thermal_insulation_products, water_supply_and_sanitation_products, construction_chemistry_products, tools_products, painting_products

urlpatterns = [
    path('dry_construction/', dry_construction_products, name='dry construction products'),
    path('thermal_insulation/', thermal_insulation_products, name='thermal insulation products'),
    path('water_supply_and_sanitation/', water_supply_and_sanitation_products, name='water supply nand sanitation products'),
    path('construction_chemistry/', construction_chemistry_products, name='construction chemistry products'),
    path('tools/', tools_products, name='tools products'),
    path('painting/', painting_products, name='painting products'),
]
