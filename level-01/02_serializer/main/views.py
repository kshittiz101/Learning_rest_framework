from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer


class BookViewsets(viewsets.ModelViewSet):

    # ascending order by id
    # queryset = Books.objects.all().order_by("id")
    # descending order by id
    queryset = Books.objects.all().order_by("-id")
    serializer_class = BookSerializer
