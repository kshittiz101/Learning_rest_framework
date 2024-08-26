from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .serializers import BookSerializer
from .models import Book
from .custom_permission import CustomPermission
class BookModelViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]
