from session_auth.models import Books
from .serializers import BooksSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# IsAuthenticatedOrReadOnly -
# IsAuthenticatedOrReadOnly is a permission class in Django REST Framework that allows:
# Safe methods (GET, HEAD, OPTIONS) for anyone (authenticated or not).
# Unsafe methods (POST, PUT, PATCH, DELETE) only for authenticated users.

# notes it is suitable when you want to give authentication user permission to read and write
#  and only want to provide read permission to unauthenticated user (anonymous users)

class BooksViewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
