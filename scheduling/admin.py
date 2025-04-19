
# Register your models here.
from django.contrib import admin
from .models import Client, Employee, ServiceCatalogue, EmployeeService, ClientAppointment, Invoice , InvoiceRow

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(ServiceCatalogue)
admin.site.register(EmployeeService)
admin.site.register(ClientAppointment)
admin.site.register(Invoice)
admin.site.register(InvoiceRow)
