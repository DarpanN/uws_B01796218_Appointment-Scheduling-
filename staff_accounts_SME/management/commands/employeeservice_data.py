import random
from django.core.management.base import BaseCommand
from scheduling.models import Employee, ServiceCatalogue, EmployeeService

class Command(BaseCommand):
    help = "Assign random services to employees without duplicates"

    def handle(self, *args, **kwargs):
        employees = list(Employee.objects.all())
        services = list(ServiceCatalogue.objects.all())

        if not employees or not services:
            self.stdout.write(self.style.ERROR("❌ No Employees or Services found!"))
            return

        EmployeeService.objects.all().delete()  # Clear existing assignments

        assignments = set()
        total_assignments = 0

        while total_assignments < min(500, len(employees) * len(services)):  # Limit entries
            employee = random.choice(employees)
            service = random.choice(services)

            # ✅ Use `employee.employee_id` instead of `employee.id`
            if (employee.employee_id, service.service_id) not in assignments:
                assignments.add((employee.employee_id, service.service_id))
                EmployeeService.objects.create(employee=employee, service=service)
                total_assignments += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {total_assignments} unique employee-service assignments added!"))
