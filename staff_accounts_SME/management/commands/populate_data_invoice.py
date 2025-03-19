from django.core.management.base import BaseCommand
from scheduling.models import Invoice, Appointment
from faker import Faker
import random

fake = Faker("en_GB")  # UK locale

class Command(BaseCommand):
    help = "Populate the Invoice table with 700 to 1000 records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with 700 to 1000 invoices...")

        appointments = list(Appointment.objects.all())

        invoices = []
        num_invoices = random.randint(700, 1000)

        for _ in range(num_invoices):
            invoice_number = f"INV{random.randint(100000, 999999)}"
            cost = round(random.uniform(50, 500), 2)
            discount = round(random.uniform(0, cost * 0.2), 2)  # Max 20% discount
            total = cost - discount

            invoices.append(Invoice(
                invoice_number=invoice_number,
                invoice_cost=cost,
                invoice_discount=discount,
                invoice_total=total,
                appointment=random.choice(appointments)
            ))

        Invoice.objects.bulk_create(invoices)
        self.stdout.write(self.style.SUCCESS(f"✅ {num_invoices} Invoices inserted!"))
