from django.urls import path

from CarCollection_app.web.views import show_index, show_catalogue,\
    show_profile, create_profile, edit_profile, delete_profile,\
    create_car, edit_car, delete_car, car_details


urlpatterns = (
    path('', show_index, name='show index'),
    path('catalogue/', show_catalogue, name='show catalogue'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('car/create/', create_car, name='create car'),
    path('car/<int:pk>/edit/', edit_car, name='edit car'),
    path('car/<int:pk>/delete/', delete_car, name='delete car'),
    path('car/<int:pk>/details/', car_details, name='car details'),
)
