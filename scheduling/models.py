from django.db import models
from django.utils.timezone import now  # Correct import for timezone handling
import datetime  # Correct import for datetime

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr'), ('Prof', 'Prof')], default='Mr')
    first_name = models.CharField(max_length=50, default='Default First Name')
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, default='Default Surname')
    address_line_1 = models.CharField(max_length=100, default='Default Address')
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, default='Default City')
    county = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=10, default='00000')
    country = models.CharField(max_length=50, default='United Kingdom')
    client_email = models.EmailField(unique=True)
    client_mobile = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.surname}"

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_payroll_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr'), ('Prof', 'Prof')], default='Mr')
    first_name = models.CharField(max_length=50, default='Default First Name')
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, default='Default Surname')
    employee_mobile = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50, choices=[('Painter', 'Painter'), ('Joiner', 'Joiner'), ('Electrician', 'Electrician'), ('Plumber', 'Plumber'), ('Manager', 'Manager')], default='Painter')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.surname}"

class ServiceCatalogue(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100, unique=True)
    service_description = models.TextField()
    service_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)

    def __str__(self):
        return self.service_name

class EmployeeService(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceCatalogue, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('employee', 'service')

    def __str__(self):
        return f"{self.employee} - {self.service}"



class ClientAppointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceCatalogue, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    appointment_duration = models.PositiveIntegerField()  # Duration in hours
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.client} with {self.employee}"

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateTimeField(default=now)
    invoice_cost = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.invoice_total = self.invoice_cost - self.invoice_discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.invoice_number}"

class InvoiceRow(models.Model):
    invoice_row_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    appointment = models.ForeignKey(ClientAppointment, on_delete=models.CASCADE)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice Row {self.invoice_row_id} for Appointment {self.appointment.appointment_id}"
