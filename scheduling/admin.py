
# Register your models here.
from django.contrib import admin
from .models import Client, Employee, Service, Appointment, Invoice

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Invoice)
