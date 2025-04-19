# from django.urls import path
# from . import views

# urlpatterns = [
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('clients/', views.client_list, name='client_list'),
#     path('employees/', views.employee_list, name='employee_list'),
#     path('services/', views.service_catalogue_list, name='service_catalogue_list'),
#     path('employee-services/', views.employee_service_list, name='employee_service_list'),
#     path('appointments/', views.appointment_list, name='appointment_list'),
#     path('invoices/', views.invoice_list, name='invoice_list'),
#     path('invoice-rows/', views.invoice_row_list, name='invoice_row_list'),
# ]


# scheduling/urls.py

from django.urls import path
from . import views  # Make sure you import the views correctly

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # This should match the view you defined above
    # Other URL patterns go here
]
