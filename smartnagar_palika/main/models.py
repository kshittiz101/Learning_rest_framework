from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = [
        ('citizen', 'citizen'),
        ('admin', 'admin'),
    ]
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, default="citizen")


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50, default="Not Provided")

    def __str__(self):
        return self.user.username


class BirthCertificate(models.Model):
    title = models.CharField(max_length=100, default="Birth Certificate")
    date_and_time_of_birth = models.DateTimeField()
    birth_place = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Application(models.Model):
    APPROVAL_STATUS = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    ]

    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    posted_date = models.DateField(auto_now_add=True)

    approval_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="approvals", null=True, blank=True
    )
    approval_date = models.DateField(null=True, blank=True)

    approval_status = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS,
        default='pending'
    )

    remarks = models.TextField(null=True, blank=True)

    birth_certificate = models.ForeignKey(
        BirthCertificate, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.birth_certificate.title} by {self.applicant}'
