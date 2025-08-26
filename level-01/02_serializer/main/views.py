from rest_framework import viewsets
from .models import Books, Snippet
from .serializers import BookSerializer, SnippetSerializer


class BookViewsets(viewsets.ModelViewSet):

    # ascending order by id
    # queryset = Books.objects.all().order_by("id")
    # descending order by id
    queryset = Books.objects.all().order_by("-id")
    serializer_class = BookSerializer


class SnippetViewsets(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
