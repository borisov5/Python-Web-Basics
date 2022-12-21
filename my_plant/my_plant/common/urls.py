from django.urls import path

from my_plant.common.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
