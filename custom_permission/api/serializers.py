from rest_framework import serializers
from api.models import Books
from django.contrib.auth import get_user_model

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    # Optional: show author's string representation (e.g., username) in book list
    # StringRelatedField() only shows the string representation (usually username or what __str__ returns).
    author = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author']
        # fields = ['id', 'title', 'price']


class AuthorSerializer(serializers.ModelSerializer):
    # Fetch all books by this author (reverse relationship via related_name="books")
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'books']
