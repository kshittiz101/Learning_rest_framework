from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .models import Book
from .serializers import BookSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
