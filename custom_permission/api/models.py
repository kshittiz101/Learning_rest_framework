from django.db import models

# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Books(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner"
    )

    def __str__(self):
        return self.title
