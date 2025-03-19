from django.core.management.base import BaseCommand
from scheduling.models import Employee
from faker import Faker
import random

fake = Faker("en_GB")  # UK locale

class Command(BaseCommand):
    help = "Populate the Employee table with 700 to 1000 records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with 700 to 1000 employees...")

        employees = []
        num_employees = random.randint(700, 1000)

        used_payroll_numbers = set()

        for _ in range(num_employees):
            full_name = fake.name()

            # Ensure the payroll number is unique
            while True:
                payroll_number = f"PAY{random.randint(10000, 99999)}"
                if payroll_number not in used_payroll_numbers:
                    used_payroll_numbers.add(payroll_number)
                    break

            phone_number = f"+44 7{random.randint(0, 9)}{random.randint(10000000, 99999999)}"

            employees.append(Employee(
                employee_payroll_number=payroll_number,
                employee_name=full_name,
                employee_mobile=phone_number
            ))

        Employee.objects.bulk_create(employees)
        self.stdout.write(self.style.SUCCESS(f"✅ {num_employees} Employees inserted!"))

