from django.core.management.base import BaseCommand
from scheduling.models import Client
from faker import Faker
import random

fake = Faker("en_GB")  # UK locale

class Command(BaseCommand):
    help = "Populate the Client table with 700 to 1000 records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with 700 to 1000 clients...")

        clients = []
        num_clients = random.randint(700, 1000)

        for _ in range(num_clients):
            full_name = fake.name()
            first_name, last_name = full_name.split(" ", 1) if " " in full_name else (full_name, "Smith")
            email_domains = ["@btinternet.com", "@gmail.com", "@hotmail.co.uk", "@yahoo.co.uk", "@outlook.com"]
            email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 99)}{random.choice(email_domains)}"
            phone_number = f"+44 7{random.randint(0, 9)}{random.randint(10000000, 99999999)}"

            clients.append(Client(
                client_name=full_name,
                client_address=fake.address(),
                client_email=email,
                client_mobile=phone_number
            ))

        Client.objects.bulk_create(clients)
        self.stdout.write(self.style.SUCCESS(f"✅ {num_clients} Clients inserted!"))


