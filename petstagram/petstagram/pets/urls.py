from django.urls import include, path

from petstagram.pets.views import add_pet, edit_pet, delete_pet, details_pet

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='delete pet'),
        path('delete/', delete_pet, name='delete pet'),
    ]))
)
