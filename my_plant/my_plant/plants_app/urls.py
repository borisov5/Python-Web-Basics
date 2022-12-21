from django.urls import path

from my_plant.plants_app.views import catalogue_page, create_plant_page, edit_plant_page, delete_plant_page, plant_details_page

urlpatterns = [
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_plant_page, name='create-plant'),
    path('<int:pk>/edit/', edit_plant_page, name='edit-plant'),
    path('<int:pk>/delete/', delete_plant_page, name='delete-plant'),
    path('<int:pk>/details/', plant_details_page, name='plant-details'),
]
