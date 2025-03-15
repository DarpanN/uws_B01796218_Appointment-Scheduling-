from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_address = models.TextField()
    client_email = models.EmailField(unique=True)
    client_mobile = models.CharField(max_length=15)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_payroll_number = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=255)
    employee_mobile = models.CharField(max_length=15)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()
    service_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
