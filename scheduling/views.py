
# # Create your views here.
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')  # Refers to global templates folder

from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Employee, Service, Appointment, Invoice
from .forms import ClientForm, EmployeeForm, ServiceForm, AppointmentForm, InvoiceForm

# CRUD for Clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})
