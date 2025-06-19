from rest_framework import serializers
from session_auth.models import Books


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author']
