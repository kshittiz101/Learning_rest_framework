# models.py
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title
