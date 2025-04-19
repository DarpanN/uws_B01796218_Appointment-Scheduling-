# dashboard/views.py
from django.shortcuts import render, redirect
from scheduling.models import Client, Employee, ServiceCatalogue, ClientAppointment, Invoice, InvoiceRow, EmployeeService
from django.utils import timezone
from django.utils.timezone import now
from django.http import HttpResponse
from decimal import Decimal 
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncDate



# Create a view function for the dashboard
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# Client Views
def client_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        client_mobile = request.POST.get('client_mobile')
        client_email = request.POST.get('client_email')
        Client.objects.create(
            title=title,
            first_name=first_name,
            surname=surname,
            client_mobile=client_mobile,
            client_email=client_email
        )
        return redirect('client_list')
    return render(request, 'dashboard/client_create.html')

# Employee Views
def employee_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        employee_mobile = request.POST.get('employee_mobile')
        employee_payroll_number = request.POST.get('employee_payroll_number')
        Employee.objects.create(
            title=title,
            first_name=first_name,
            surname=surname,
            employee_mobile=employee_mobile,
            employee_payroll_number=employee_payroll_number
        )
        return redirect('employee_list')
    return render(request, 'dashboard/employee_create.html')

# Service Catalogue Views
def service_catalogue_create(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_description = request.POST.get('service_description')
        service_hourly_rate = request.POST.get('service_hourly_rate')
        vat_rate = request.POST.get('vat_rate')
        ServiceCatalogue.objects.create(
            service_name=service_name,
            service_description=service_description,
            service_hourly_rate=service_hourly_rate,
            vat_rate=vat_rate
        )
        return redirect('service_catalogue')
    return render(request, 'dashboard/service_catalogue_create.html')

# # Client Appointment Views

def appointment_create(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        employee_id = request.POST.get('employee')
        service_id = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')
        appointment_duration = request.POST.get('appointment_duration')
        expenses = request.POST.get('expenses')
        status = request.POST.get('status')

        # Create the appointment
        ClientAppointment.objects.create(
            client_id=client_id,
            employee_id=employee_id,
            service_id=service_id,
            appointment_date=appointment_date,
            appointment_duration=appointment_duration,
            expenses=expenses,
            status=status,
            created_at=now()
        )
        return redirect('appointments_list')  # Change this to your actual URL name for redirect

    # GET request – fetch data to populate dropdowns
    clients = Client.objects.all()
    employees = Employee.objects.all()
    services = ServiceCatalogue.objects.all()

    return render(request, 'dashboard/appointment_create.html', {
        'clients': clients,
        'employees': employees,
        'services': services
    })



#updated invoice 
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Client, ClientAppointment, Employee, ServiceCatalogue, Invoice, InvoiceRow
from .forms import InvoiceForm
from django.db import transaction

def create_invoice(request):
    clients = Client.objects.all()
    appointments = ClientAppointment.objects.all()
    employees = Employee.objects.all()
    services = ServiceCatalogue.objects.all()

    invoice_form = InvoiceForm()

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)

        if invoice_form.is_valid():
            # Start a transaction to ensure atomicity
            with transaction.atomic():
                # Save the invoice form data
                invoice = invoice_form.save(commit=False)

                # Calculate total (this could be based on the selected appointments/services)
                invoice_cost = invoice_form.cleaned_data['invoice_cost']
                invoice_discount = invoice_form.cleaned_data['invoice_discount']
                invoice.invoice_total = invoice_cost - invoice_discount
                invoice.save()

                # Add invoice rows based on the selected appointments (you can modify this as per your needs)
                appointment_id = request.POST.get('appointment')
                appointment = ClientAppointment.objects.get(id=appointment_id)
                
                # Create invoice rows
                invoice_row = InvoiceRow(invoice=invoice, appointment=appointment, service_cost=appointment.service.service_hourly_rate)
                invoice_row.save()

                return redirect('invoice_report', invoice_id=invoice.id)

    context = {
        'invoice_form': invoice_form,
        'clients': clients,
        'appointments': appointments,
        'employees': employees,
        'services': services,
    }

    return render(request, 'dashboard/invoices/form.html', context)




###


from django.shortcuts import render, redirect
from django.db import transaction
from .forms import InvoiceForm
# from .models import ClientAppointment, InvoiceRow

def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        if invoice_form.is_valid():
            with transaction.atomic():
                invoice = invoice_form.save(commit=False)
                invoice.invoice_total = invoice.invoice_cost - invoice.invoice_discount
                invoice.save()

                appointment = invoice_form.cleaned_data['appointment']
                invoice_row = InvoiceRow(
                    invoice=invoice,
                    appointment=appointment,
                    service_cost=appointment.service.service_hourly_rate
                )
                invoice_row.save()

                return redirect('invoice_report', invoice_id=invoice.id)
    else:
        invoice_form = InvoiceForm()

    return render(request, 'dashboard/invoices/form.html', {'invoice_form': invoice_form})




from django.shortcuts import render, redirect
from django.db import transaction
from .forms import InvoiceForm
from scheduling.models import InvoiceRow

def create_invoice(request):
    invoice_form = InvoiceForm()

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)

        if invoice_form.is_valid():
            with transaction.atomic():
                invoice = invoice_form.save(commit=False)
                invoice.invoice_total = invoice.invoice_cost - invoice.invoice_discount
                invoice.save()

                # Get appointment from form
                appointment = invoice_form.cleaned_data['appointment']

                # Create related invoice row
                InvoiceRow.objects.create(
                    invoice=invoice,
                    appointment=appointment,
                    service_cost=appointment.service.service_hourly_rate
                )

                return redirect('invoice_report', invoice_id=invoice.id)

    return render(request, 'dashboard/invoices/form.html', {'invoice_form': invoice_form})



def invoice_report(request, invoice_id):
    return render(request, 'dashboard/invoices/report.html', {'invoice_id': invoice_id})


def view_invoice(request, invoice_id):
    # Fetch the invoice using the provided ID
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    context = {
        'invoice': invoice
    }

    return render(request, 'dashboard/invoice.html', context)






#-------------
# def create_invoice(request):
#     if request.method == 'POST':
#         invoice_form = InvoiceForm(request.POST)
#         if invoice_form.is_valid():
#             with transaction.atomic():
#                 invoice = invoice_form.save(commit=False)

#                 invoice_cost = invoice_form.cleaned_data['invoice_cost']
#                 invoice_discount = invoice_form.cleaned_data['invoice_discount']
#                 invoice.invoice_total = invoice_cost - invoice_discount
#                 invoice.save()

#                 # Get appointment from cleaned_data
#                 appointment = invoice_form.cleaned_data['appointment']
#                 invoice_row = InvoiceRow(
#                     invoice=invoice,
#                     appointment=appointment,
#                     service_cost=appointment.service.service_hourly_rate
#                 )
#                 invoice_row.save()

#                 return redirect('invoice_report', invoice_id=invoice.id)
#     else:
#         invoice_form = InvoiceForm()

#     return render(request, 'dashboard/invoices/form.html', {'invoice_form': invoice_form})








def invoice_report(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    invoice_rows = InvoiceRow.objects.filter(invoice=invoice)
    
    context = {
        'invoice': invoice,
        'invoice_rows': invoice_rows,
    }

    return render(request, 'dashboard/invoices/report.html', context)
























# Invoice Row Views
def invoice_row_create(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        appointment_id = request.POST.get('appointment_id')
        service_cost = request.POST.get('service_cost')
        InvoiceRow.objects.create(
            invoice_id=invoice_id,
            appointment_id=appointment_id,
            service_cost=service_cost
        )
        return redirect('invoice_row_list')
    return render(request, 'dashboard/invoice_row_create.html')

# Employee Service Views
def employee_service_create(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        service_id = request.POST.get('service_id')
        EmployeeService.objects.create(
            employee_id=employee_id,
            service_id=service_id
        )
        return redirect('employee_service_list')
    return render(request, 'dashboard/employee_service_create.html')




from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    ClientForm, EmployeeForm, ClientAppointmentForm, 
    ServiceCatalogueForm, InvoiceForm, InvoiceRowForm, EmployeeServiceForm
)
from scheduling.models import (
    Client, Employee, ClientAppointment,
    ServiceCatalogue, Invoice, InvoiceRow, EmployeeService
)

from django.core.paginator import Paginator



# Dashboard home
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


### CRUD for Client
# def client_list(request):
#     clients = Client.objects.all()
#     return render(request, 'dashboard/clients/list.html', {'clients': clients})

# Client List View
def client_list(request):
    client_list = Client.objects.all().order_by('client_id')
    paginator = Paginator(client_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/clients/list.html', {'page_obj': page_obj})



def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'dashboard/clients/form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'dashboard/clients/form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')


### CRUD for Employee
# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'dashboard/employees/list.html', {'employees': employees})

def employee_list(request):
    employee_list = Employee.objects.all().order_by('employee_id')  # you can order as you like
    paginator = Paginator(employee_list, 100)  # Show 100 employees per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/employees/list.html', {'page_obj': page_obj})



def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'dashboard/employees/form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'dashboard/employees/form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')


### CRUD for ClientAppointment
# def appointment_list(request):
#     appointments = ClientAppointment.objects.all()
#     return render(request, 'dashboard/appointments/list.html', {'appointments': appointments})


# def appointment_list(request):
#     appointment_list = ClientAppointment.objects.all().order_by('appointment_id')
#     paginator = Paginator(appointment_list, 100)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'dashboard/appointments/list.html', {'page_obj': page_obj})
# def appointment_create(request):
#     if request.method == 'POST':
#         form = ClientAppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('appointment_list')
#     else:
#         form = ClientAppointmentForm()
#     return render(request, 'dashboard/appointments/form.html', {'form': form})




# def appointment_update(request, appointment_id):
#     # Fetch the appointment instance that you want to update
#     appointment = get_object_or_404(ClientAppointment, id=appointment_id)

#     # Handle POST request (form submission)
#     if request.method == 'POST':
#         form = ClientAppointmentForm(request.POST, instance=appointment)
#         if form.is_valid():
#             form.save()
#             return redirect('appointments_list')  # Redirect to the appropriate page after saving
#     else:
#         # If it's a GET request, pre-populate the form with the existing appointment data
#         form = ClientAppointmentForm(instance=appointment)

#     return render(request, 'appointment_form.html', {'form': form})




def appointment_list(request):
    # Get today's date
    today = timezone.localdate()

    # Get all appointments
    appointments = ClientAppointment.objects.all()

    # Filter appointments for today
    todays_appointments = appointments.filter(appointment_date__date=today)

    # Count today's appointments
    todays_appointments_count = todays_appointments.count()

    # Paginate the appointment list
    paginator = Paginator(appointments, 100)  # 100 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template and pass the context
    return render(request, 'dashboard/appointments/list.html', {
        'page_obj': page_obj,
        'todays_appointments_count': todays_appointments_count,
    })





def appointment_update(request, pk):
    appointment = get_object_or_404(ClientAppointment, pk=pk)
    if request.method == 'POST':
        form = ClientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = ClientAppointmentForm(instance=appointment)
    return render(request, 'dashboard/appointments/form.html', {'form': form})

def appointment_delete(request, pk):
    appointment = get_object_or_404(ClientAppointment, pk=pk)
    appointment.delete()
    return redirect('appointment_list')


### CRUD for ServiceCatalogue
# def service_catalogue_list(request):
#     services = ServiceCatalogue.objects.all()
#     return render(request, 'dashboard/services/list.html', {'services': services})

def service_catalogue_list(request):
    service_list = ServiceCatalogue.objects.all().order_by('service_id')
    paginator = Paginator(service_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/services/list.html', {'page_obj': page_obj})



def service_catalogue_create(request):
    if request.method == 'POST':
        form = ServiceCatalogueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_catalogue_list')
    else:
        form = ServiceCatalogueForm()
    return render(request, 'dashboard/services/form.html', {'form': form})

def service_catalogue_update(request, pk):
    service = get_object_or_404(ServiceCatalogue, pk=pk)
    if request.method == 'POST':
        form = ServiceCatalogueForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_catalogue_list')
    else:
        form = ServiceCatalogueForm(instance=service)
    return render(request, 'dashboard/services/form.html', {'form': form})

def service_catalogue_delete(request, pk):
    service = get_object_or_404(ServiceCatalogue, pk=pk)
    service.delete()
    return redirect('service_catalogue_list')


### CRUD for Invoice
# def invoice_list(request):
#     invoices = Invoice.objects.all()
#     return render(request, 'dashboard/invoices/list.html', {'invoices': invoices})

def invoice_list(request):
    invoice_list = Invoice.objects.all().order_by('invoice_id')
    paginator = Paginator(invoice_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/invoices/list.html', {'page_obj': page_obj})


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'dashboard/invoices/form.html', {'form': form})

def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'dashboard/invoices/form.html', {'form': form})

def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.delete()
    return redirect('invoice_list')


### CRUD for InvoiceRow
# def invoice_row_list(request):
#     rows = InvoiceRow.objects.all()
#     return render(request, 'dashboard/invoice_rows/list.html', {'rows': rows})

def invoice_row_list(request):
    invoice_row_list = InvoiceRow.objects.all().order_by('invoice_row_id')
    paginator = Paginator(invoice_row_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/invoice_rows/list.html', {'page_obj': page_obj})


def invoice_row_create(request):
    if request.method == 'POST':
        form = InvoiceRowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_row_list')
    else:
        form = InvoiceRowForm()
    return render(request, 'dashboard/invoice_rows/form.html', {'form': form})

def invoice_row_update(request, pk):
    row = get_object_or_404(InvoiceRow, pk=pk)
    if request.method == 'POST':
        form = InvoiceRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return redirect('invoice_row_list')
    else:
        form = InvoiceRowForm(instance=row)
    return render(request, 'dashboard/invoice_rows/form.html', {'form': form})

def invoice_row_delete(request, pk):
    row = get_object_or_404(InvoiceRow, pk=pk)
    row.delete()
    return redirect('invoice_row_list')


### CRUD for EmployeeService
# def employee_service_list(request):
#     entries = EmployeeService.objects.all()
#     return render(request, 'dashboard/employee_services/list.html', {'entries': entries})

def employee_service_list(request):
    employee_service_list = EmployeeService.objects.all().order_by('id')
    paginator = Paginator(employee_service_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/employee_services/list.html', {'page_obj': page_obj})

def employee_service_create(request):
    if request.method == 'POST':
        form = EmployeeServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_service_list')
    else:
        form = EmployeeServiceForm()
    return render(request, 'dashboard/employee_services/form.html', {'form': form})

def employee_service_update(request, pk):
    entry = get_object_or_404(EmployeeService, pk=pk)
    if request.method == 'POST':
        form = EmployeeServiceForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('employee_service_list')
    else:
        form = EmployeeServiceForm(instance=entry)
    return render(request, 'dashboard/employee_services/form.html', {'form': form})

def employee_service_delete(request, pk):
    entry = get_object_or_404(EmployeeService, pk=pk)
    entry.delete()
    return redirect('employee_service_list')




# from django.shortcuts import render
from django.db.models import Q
# from .models import Client, Employee, ServiceCatalogue, ClientAppointment, Invoice, InvoiceRow

def search_results(request):
    query = request.GET.get('query', '')
    clients = []
    employees = []
    services = []
    appointments = []
    invoices = []
    invoice_rows = []

    # Perform search if there's a query
    if query:
        # Search in Client model
        if query.isdigit():  # If query is numeric, treat it as ID
            clients = Client.objects.filter(client_id=query)
        else:  # Otherwise, search by phone number or name
            clients = Client.objects.filter(
                Q(client_mobile__icontains=query) | 
                Q(first_name__icontains=query) |
                Q(surname__icontains=query)
            )

        # Search in Employee model
        if query.isdigit():  # If query is numeric, treat it as employee ID
            employees = Employee.objects.filter(employee_id=query)
        else:  # Search by name or mobile
            employees = Employee.objects.filter(
                Q(first_name__icontains=query) | 
                Q(surname__icontains=query) | 
                Q(employee_mobile__icontains=query)
            )

        # Search in ServiceCatalogue model by service ID or name
        if query.isdigit():
            services = ServiceCatalogue.objects.filter(service_id=query)
        else:
            services = ServiceCatalogue.objects.filter(service_name__icontains=query)

        # Search in Appointment model
        if query.isdigit():
            appointments = ClientAppointment.objects.filter(appointment_id=query)
        else:
            appointments = ClientAppointment.objects.filter(
                Q(client__first_name__icontains=query) | 
                Q(client__surname__icontains=query) | 
                Q(client__client_mobile__icontains=query)
            )

        # Search in Invoice model
        if query.isdigit():
            invoices = Invoice.objects.filter(invoice_id=query)
        else:
            invoices = Invoice.objects.filter(invoice_number__icontains=query)

        # Search in InvoiceRow model
        if query.isdigit():
            invoice_rows = InvoiceRow.objects.filter(invoice_row_id=query)
        else:
            invoice_rows = InvoiceRow.objects.filter(
                Q(appointment__client__first_name__icontains=query) | 
                Q(appointment__client__surname__icontains=query)
            )

    return render(request, 'dashboard/search_results.html', {
        'query': query,
        'clients': clients,
        'employees': employees,
        'services': services,
        'appointments': appointments,
        'invoices': invoices,
        'invoice_rows': invoice_rows
    })



def create_invoice(request):
    return HttpResponse("Invoice generation page (to be implemented).")



def services_by_month(request):
    services = (
        ClientAppointment.objects
        .annotate(month=TruncMonth('appointment_date'))
        .values('month', 'service__service_name')
        .annotate(count=Count('appointment_id'))
        .order_by('month')
    )

    context = {'services': services}
    return render(request, 'dashboard/reports/services_by_month.html', context)



def income_by_month(request):
    income = (
        Invoice.objects
        .annotate(month=TruncMonth('invoice_date'))
        .values('month')
        .annotate(total_income=Sum('invoice_total'))
        .order_by('month')
    )

    context = {'income': income}
    return render(request, 'dashboard/reports/income_by_month.html', context)



# def income_by_day(request):
#     invoices = Invoice.objects.annotate(invoice_day=TruncDate('invoice_date')) \
#                               .values('invoice_day') \
#                               .annotate(total_income=Sum('invoice_cost')) \
#                               .order_by('invoice_day')
#     return render(request, 'dashboard/reports/income_by_day.html', {'invoices': invoices})






# from django.shortcuts import render
# from decimal import Decimal
# from django.utils.timezone import now
# from .models import Invoice, InvoiceRow, ClientAppointment

def generate_invoice_view(request):
    invoice = None

    if request.method == 'POST':
        invoice_number = request.POST.get('invoice_number')
        appointment_ids_str = request.POST.get('appointment_ids')
        discount_str = request.POST.get('discount')

        appointment_ids = [int(i.strip()) for i in appointment_ids_str.split(',') if i.strip().isdigit()]
        discount = Decimal(discount_str or '0.00')

        try:
            invoice = generate_invoice(appointment_ids, invoice_number, discount)
        except Exception as e:
            return render(request, 'generate_invoice.html', {
                'error': str(e)
            })

    return render(request, 'generate_invoice.html', {'invoice': invoice})


def generate_invoice(appointment_ids, invoice_number, discount=0):
    appointments = ClientAppointment.objects.filter(appointment_id__in=appointment_ids)

    if not appointments.exists():
        raise ValueError("No valid appointments found.")

    total_cost = Decimal('0.00')
    invoice = Invoice(
        invoice_number=invoice_number,
        invoice_cost=0,
        invoice_discount=Decimal(discount),
        invoice_total=0
    )
    invoice.save()

    for appt in appointments:
        hourly_rate = appt.service.service_hourly_rate
        duration = appt.appointment_duration
        expenses = appt.expenses
        vat_rate = appt.service.vat_rate / 100

        service_cost_before_vat = (hourly_rate * duration) + expenses
        service_cost_with_vat = service_cost_before_vat * (1 + vat_rate)

        InvoiceRow.objects.create(
            invoice=invoice,
            appointment=appt,
            service_cost=service_cost_with_vat.quantize(Decimal('0.01'))
        )

        total_cost += service_cost_with_vat

    invoice.invoice_cost = total_cost
    invoice.save()
    return invoice