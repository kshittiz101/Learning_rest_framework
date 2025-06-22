from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
