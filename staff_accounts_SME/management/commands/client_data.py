import os
import django
from faker import Faker
from django.utils.timezone import now
from scheduling.models import Client  # Ensure this is the correct import path

# Setup Django Environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Replace 'your_project' with your Django project name
django.setup()

# Initialize Faker with UK locale
fake = Faker(["en_GB"])  # UK-based faker

# Titles available
TITLES = ['Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Prof']

# Generate and insert 1000 client records
def create_clients(n=1000):
    clients = []  # Use bulk_create for efficiency
    for _ in range(n):
        client = Client(
            title=fake.random_element(TITLES),
            first_name=fake.first_name(),
            middle_name=fake.first_name() if fake.boolean() else None,
            surname=fake.last_name(),
            address_line_1=fake.street_address(),
            address_line_2=fake.secondary_address() if fake.boolean() else None,
            city=fake.city(),
            county=fake.county() if fake.boolean() else None,
            postcode=fake.postcode(),
            country="United Kingdom",
            client_email=fake.unique.email(),
            client_mobile=fake.unique.phone_number(),
            created_at=now()
        )
        clients.append(client)

    # Bulk insert all records (faster than individual saves)
    Client.objects.bulk_create(clients)
    print(f"Successfully created {n} UK-based clients!")

# Run data generation
create_clients(1000)
