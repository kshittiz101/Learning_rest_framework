from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Books(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Books"
