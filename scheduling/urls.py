from django.urls import path
from .views import client_list, client_create, client_update, client_delete

urlpatterns = [
    path('clients/', client_list, name='client_list'),
    path('clients/new/', client_create, name='client_create'),
    path('clients/<int:pk>/edit/', client_update, name='client_update'),
    path('clients/<int:pk>/delete/', client_delete, name='client_delete'),
]
