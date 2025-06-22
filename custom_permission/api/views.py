from api.models import Books
from api.serializers import BookSerializer
from rest_framework import viewsets


class BookViewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
