import random
from django.core.management.base import BaseCommand
from faker import Faker
from scheduling.models import Employee
from django.utils.timezone import now

class Command(BaseCommand):
    help = "Generate 1000 random employee records"

    def handle(self, *args, **kwargs):
        fake = Faker(["en_GB"])  # UK format
        roles = ["Painter", "Joiner", "Electrician", "Plumber", "Manager"]
        titles = ["Mr", "Mrs", "Miss", "Ms", "Dr", "Prof"]

        employees = []

        for _ in range(1000):
            employee = Employee(
                employee_payroll_number=fake.unique.bothify(text="EMP###???"),  # Random payroll number
                title=random.choice(titles),
                first_name=fake.first_name(),
                middle_name=fake.first_name() if random.random() > 0.5 else None,  # 50% chance of a middle name
                surname=fake.last_name(),
                employee_mobile=fake.unique.phone_number(),
                role=random.choice(roles),
                created_at=now(),
            )
            employees.append(employee)

        Employee.objects.bulk_create(employees)  # Bulk insert for efficiency

        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(employees)} employees!"))

