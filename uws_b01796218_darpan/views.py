from django.http import HttpResponse

def client_list(request):
    return HttpResponse("Client List Page")

def employee_list(request):
    return HttpResponse("Employee List Page")
