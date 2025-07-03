from django.contrib.auth.models import AbstractUser

from django.db import models

# create custom user model


class User(AbstractUser):
    USER_TYPES = [
        ('citizen', 'citizen'),
        ('admin', 'admin'),
    ]

    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, default="citizen")

# profile db


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50, default="Not Provided")

    def __str__(self):
        return self.user.username
