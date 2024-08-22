from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializers):
    class Meta:
        model = Book
        fields = '__all__'