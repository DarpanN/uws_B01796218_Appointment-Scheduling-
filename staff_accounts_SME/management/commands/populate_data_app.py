from django.core.management.base import BaseCommand
from scheduling.models import Appointment, Client, Employee, Service_Catalogue
from faker import Faker
import random

fake = Faker("en_GB")  # UK locale

class Command(BaseCommand):
    help = "Populate the Appointment table with 700 to 1000 records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with 700 to 1000 appointments...")

        clients = list(Client.objects.all())
        employees = list(Employee.objects.all())
        services = list(Service_Catalogue.objects.all())

        appointments = []
        num_appointments = random.randint(700, 1000)

        for _ in range(num_appointments):
            appointment_date = fake.date_between(start_date="-1y", end_date="+1y")
            cost = round(random.uniform(50, 500), 2)
            expenses = round(random.uniform(10, 50), 2)

            appointments.append(Appointment(
                client=random.choice(clients),
                employee=random.choice(employees),
                service=random.choice(services),
                appointment_date=appointment_date,
                cost=cost,
                expenses=expenses
            ))

        Appointment.objects.bulk_create(appointments)
        self.stdout.write(self.style.SUCCESS(f"✅ {num_appointments} Appointments inserted!"))
