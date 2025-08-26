from django.db import models
# from django.utils import timezone

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    # auto_now_add is not changed
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # auto_now will changed when ever save() or update() is called,
    #  it will changed to the currernt Time stamp
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
