# from django.shortcuts import render
# from scheduling.models import Client, Employee, ServiceCatalogue, ClientAppointment, Invoice, InvoiceRow, EmployeeService

# # Example view to display client list
# def client_list(request):
#     clients = Client.objects.all()  # Retrieve all clients from the Client model
#     return render(request, 'scheduling/client_list.html', {'clients': clients})

# # Example view to display employee list
# def employee_list(request):
#     employees = Employee.objects.all()  # Retrieve all employees from the Employee model
#     return render(request, 'scheduling/employee_list.html', {'employees': employees})

# # Example view to display service catalogue
# def service_catalogue(request):
#     services = ServiceCatalogue.objects.all()  # Retrieve all services from the ServiceCatalogue model
#     return render(request, 'scheduling/service_catalogue.html', {'services': services})

# # Example view to display client appointments
# def appointment_list(request):
#     appointments = ClientAppointment.objects.all()  # Retrieve all appointments from the ClientAppointment model
#     return render(request, 'scheduling/appointment_list.html', {'appointments': appointments})

# # Example view to display invoices
# def invoice_list(request):
#     invoices = Invoice.objects.all()  # Retrieve all invoices from the Invoice model
#     return render(request, 'scheduling/invoice_list.html', {'invoices': invoices})

# # Example view to display invoice rows
# def invoice_row_list(request):
#     invoice_rows = InvoiceRow.objects.all()  # Retrieve all invoice rows from the InvoiceRow model
#     return render(request, 'scheduling/invoice_row_list.html', {'invoice_rows': invoice_rows})

# # Example view to display employee services
# def employee_service_list(request):
#     employee_services = EmployeeService.objects.all()  # Retrieve all employee services from the EmployeeService model
#     return render(request, 'scheduling/employee_service_list.html', {'employee_services': employee_services})



# scheduling/views.py
from django.shortcuts import render

# Define the dashboard view
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')  # Ensure this path is correct
