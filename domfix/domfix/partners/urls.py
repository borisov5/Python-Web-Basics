from django.urls import path, include

from domfix.partners.views import show_partners, add_partner, delete_partner, edit_partner

urlpatterns = (
    path('', show_partners, name='show partners'),
    path('add/', add_partner, name='add partner'),
    path('<int:pk>/', include([
        path('delete', delete_partner, name='delete partner'),
        path('edit',edit_partner, name='edit partner'),
    ])),
)