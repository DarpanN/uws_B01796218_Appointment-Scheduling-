from django import forms
from .models import Client, Employee, Service_Catalogue, Appointment, Invoice

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class Service_CatalogueForm(forms.ModelForm):
    class Meta:
        model = Service_Catalogue
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
