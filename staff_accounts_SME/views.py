from django.urls import path
from .views import dashboard, client_list, employee_list, service_list, appointment_list, invoice_list

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('clients/', client_list, name='client_list'),
    path('employees/', employee_list, name='employee_list'),
    path('services/', service_list, name='service_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('invoices/', invoice_list, name='invoice_list'),
]
