from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class StaffUser(AbstractUser):
    """ Custom user model for staff accounts. """

    # Avoid conflicts by specifying unique related names
    groups = models.ManyToManyField(Group, related_name="staff_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="staff_users_permissions", blank=True)
