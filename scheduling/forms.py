from django import forms
from .models import Client, Employee, ServiceCatalogue, EmployeeService, ClientAppointment, Invoice, InvoiceRow

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ServiceCatalogueForm(forms.ModelForm):
    class Meta:
        model = ServiceCatalogue
        fields = '__all__'

class EmployeeServiceForm(forms.ModelForm):
    class Meta:
        model = EmployeeService
        fields = '__all__'

class ClientAppointmentForm(forms.ModelForm):
    class Meta:
        model = ClientAppointment
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceRowForm(forms.ModelForm):
    class Meta:
        model = InvoiceRow
        fields = '__all__'
