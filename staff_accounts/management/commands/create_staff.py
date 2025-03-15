from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create staff user accounts"

    def handle(self, *args, **kwargs):
        staff_users = [
            {"username": "B01802556", "email": "sbhujel@example.com", "password": "userone", "first_name": "Sanjay", "last_name": "Bhujel"},
            {"username": "B01755961", "email": "nbhomjan@example.com", "password": "usertwo", "first_name": "Nikesh", "last_name": "Bhomjan"},
            {"username": "B01802561 ", "email": "pchaudhary@example.com", "password": "userthree", "first_name": "Prakash", "last_name": "Chaudhary"},
        ]

        for user_data in staff_users:
            if not User.objects.filter(username=user_data["username"]).exists():
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=user_data["password"]
                )
                user.first_name = user_data["first_name"]
                user.last_name = user_data["last_name"]
                user.is_staff = True  # Gives staff access to the admin panel
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created staff user: {user.username}"))
            else:
                self.stdout.write(self.style.WARNING(f"User {user_data['username']} already exists."))
