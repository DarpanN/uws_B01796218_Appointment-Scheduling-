from django import forms
from scheduling.models import (
    Client,
    Employee,
    ClientAppointment,
    ServiceCatalogue,
    Invoice,
    InvoiceRow,
    EmployeeService
)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ClientAppointmentForm(forms.ModelForm):
    class Meta:
        model = ClientAppointment
        fields = '__all__'


class ClientAppointmentForm(forms.ModelForm):
    class Meta:
        model = ClientAppointment
        fields = ['client', 'employee', 'service', 'appointment_date', 'appointment_duration']

class ServiceCatalogueForm(forms.ModelForm):
    class Meta:
        model = ServiceCatalogue
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceRowForm(forms.ModelForm):
    class Meta:
        model = InvoiceRow
        fields = '__all__'






class EmployeeServiceForm(forms.ModelForm):
    class Meta:
        model = EmployeeService
        fields = '__all__'



class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)












class InvoiceForm(forms.ModelForm):
    appointment = forms.ModelChoiceField(
        queryset=ClientAppointment.objects.filter(status='Completed'),
        label='Select Appointment',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'invoice_date', 'invoice_cost', 'invoice_discount', 'appointment']
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'invoice_discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }








class InvoiceRowForm(forms.ModelForm):
    class Meta:
        model = InvoiceRow
        fields = ['appointment', 'service_cost']

class ClientAppointmentForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    appointment = forms.ModelChoiceField(queryset=ClientAppointment.objects.none())  # Appointment will be dynamically filled based on client
    employee = forms.ModelChoiceField(queryset=Employee.objects.none())  # Employee will be dynamically filled based on appointment
    service = forms.ModelChoiceField(queryset=ServiceCatalogue.objects.none())  # Services available based on employee role or catalogue


from django.shortcuts import render, get_object_or_404, redirect
from scheduling.forms import ClientAppointmentForm



def appointment_update(request, appointment_id):
    # Fetch the appointment instance that you want to update
    appointment = get_object_or_404(ClientAppointment, id=appointment_id)

    # Handle POST request (form submission)
    if request.method == 'POST':
        form = ClientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')  # Redirect to the appropriate page after saving
    else:
        # If it's a GET request, pre-populate the form with the existing appointment data
        form = ClientAppointmentForm(instance=appointment)

    return render(request, 'form.html', {'form': form})
