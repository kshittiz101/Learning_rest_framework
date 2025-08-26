# serializers.py
from rest_framework import serializers
from .models import Author, Book

# Small item serializer to reuse


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price"]


class AuthorSerializer(serializers.ModelSerializer):
    # Reverse nesting (Author -> Books)
    # Read-only list of books per author
    books = BookMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]


class AuthorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    # Nested author for READS
    author = AuthorMiniSerializer(read_only=True)
    # ID field for WRITES
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author",
        write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id", "title", "desc", "price",
            "author",       # read
            "author_id"     # write
        ]

    # Optional: field-level validation examples
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    # Optional: object-level example (cross-field)
    def validate(self, attrs):
        title = attrs.get("title") or getattr(self.instance, "title", "")
        price = attrs.get("price") if "price" in attrs else getattr(
            self.instance, "price", None)
        if "premium" in title.lower() and price is not None and price < 50:
            raise serializers.ValidationError(
                "Premium books must cost at least 50.")
        return attrs
