import random
from faker import Faker
from django.core.management.base import BaseCommand
from scheduling.models import ServiceCatalogue

fake = Faker()

class Command(BaseCommand):
    help = "Generate 100 unique random services in the Service Catalogue"

    def handle(self, *args, **kwargs):
        services_list = [
            "Indoor Painting", "Exterior Painting", "Joinery", "Plumbing",
            "Electrical Work", "Flooring", "Roofing", "Tiling", "Carpentry",
            "Landscaping", "Wall Plastering", "Home Renovation", "Furniture Assembly",
            "Heating Repair", "Window Cleaning", "Gutter Cleaning", "Kitchen Fitting",
            "Bathroom Fitting", "Fencing", "Decking", "Patio Installation", "Pest Control"
        ]

        ServiceCatalogue.objects.all().delete()  # Clear existing data

        unique_services = set()
        while len(unique_services) < 100:
            service_name = random.choice(services_list) + " " + fake.unique.word().capitalize()
            if not ServiceCatalogue.objects.filter(service_name=service_name).exists():
                unique_services.add(service_name)

        for service_name in unique_services:
            service_description = fake.sentence(nb_words=15)
            service_hourly_rate = round(random.uniform(25, 150), 2)
            vat_rate = 20.00

            ServiceCatalogue.objects.create(
                service_name=service_name,
                service_description=service_description,
                service_hourly_rate=service_hourly_rate,
                vat_rate=vat_rate
            )

        self.stdout.write(self.style.SUCCESS("✅ 100 unique random services added!"))
