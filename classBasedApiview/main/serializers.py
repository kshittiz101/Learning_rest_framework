from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError(
                "ISBN must be 10 or 13 characters long.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value
