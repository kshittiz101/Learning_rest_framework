from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]