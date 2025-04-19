from django.http import HttpResponse

def client_list(request):
    return HttpResponse("Client List Page")

def employee_list(request):
    return HttpResponse("Employee List Page")

def employee_service_list(request):
    return HttpResponse("Employee Service List Page")

def clientappointment_list(request):
    return HttpResponse("Client Appointment List Page")

def invoice_list(request):
    return HttpResponse("Invoice List Page")

def invoicerow_list(request):
    return HttpResponse("Invoice List Page")
