from django.urls import path

from domfix.common.views import index, contacts_page

urlpatterns = (
    path('', index, name='index'),
    path('contacts/', contacts_page, name='contact page'),
)