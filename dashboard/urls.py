# dashboard/urls.py
from django.urls import path
from . import views
from scheduling.models import Client


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Client CRUD
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    # Employee CRUD
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Service CRUD
    path('services/', views.service_catalogue_list, name='service_catalogue_list'),
    path('services/add/', views.service_catalogue_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_catalogue_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_catalogue_delete, name='service_delete'),

    # Appointment CRUD
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    # Invoice CRUD
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/edit/', views.invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),

    # InvoiceRow CRUD
    path('invoice-rows/', views.invoice_row_list, name='invoice_row_list'),
    path('invoice-rows/add/', views.invoice_row_create, name='invoice_row_create'),
    path('invoice-rows/<int:pk>/edit/', views.invoice_row_update, name='invoice_row_update'),
    path('invoice-rows/<int:pk>/delete/', views.invoice_row_delete, name='invoice_row_delete'),

    # EmployeeService CRUD
    path('employee-services/', views.employee_service_list, name='employee_service_list'),
    path('employee-services/add/', views.employee_service_create, name='employee_service_create'),
    path('employee-services/<int:pk>/edit/', views.employee_service_update, name='employee_service_update'),
    path('employee-services/<int:pk>/delete/', views.employee_service_delete, name='employee_service_delete'),

    # Search
    path('search_results/', views.search_results, name='search_results'),

#invoice generate
    path('create-invoice/', views.create_invoice, name='create_invoice'),
#service-by-month
    path('reports/services-by-month/', views.services_by_month, name='services_by_month'),

#income-by-month
    path('reports/income-by-month/', views.income_by_month, name='income_by_month'),

#income by day
# path('reports/income-by-day/', views.income_by_day, name='income_by_day'),

    path('appointments/', views.appointment_list, name='appointments_list'),


    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('invoice_report/<int:invoice_id>/', views.invoice_report, name='invoice_report'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:invoice_id>/report/', views.invoice_report, name='invoice_report'),


]
