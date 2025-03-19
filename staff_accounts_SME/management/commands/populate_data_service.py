from django.core.management.base import BaseCommand
from scheduling.models import Service_Catalogue
from faker import Faker
import random

fake = Faker("en_GB")  # UK locale

class Command(BaseCommand):
    help = "Populate the Service_Catalogue table with 700 to 1000 records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with 700 to 1000 services...")

        services = []
        num_services = random.randint(700, 1000)
        service_names = ["Plumbing", "Electric Repair", "Carpentry", "House Cleaning", "Gardening", "Painting", "Roof Repair"]

        for _ in range(num_services):
            services.append(Service_Catalogue(
                service_name=random.choice(service_names),
                service_description=fake.sentence(nb_words=10),
                service_hourly_rate=round(random.uniform(20, 100), 2)
            ))

        Service_Catalogue.objects.bulk_create(services)
        self.stdout.write(self.style.SUCCESS(f"✅ {num_services} Service Catalogue records inserted!"))
