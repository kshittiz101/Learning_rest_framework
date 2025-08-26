from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id', 'title', 'description',
            'price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at']
