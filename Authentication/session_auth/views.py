from session_auth.models import Books
from .serializers import BooksSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class BooksViewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
