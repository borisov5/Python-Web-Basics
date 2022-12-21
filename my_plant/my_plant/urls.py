from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_plant.common.urls')),
    path('profile/', include('my_plant.auth_app.urls')),
    path('plant/', include('my_plant.plants_app.urls')),
]
