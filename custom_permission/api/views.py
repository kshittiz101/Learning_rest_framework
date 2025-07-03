from api.models import Books
from api.serializers import BookSerializer
from rest_framework import viewsets
from api.custom_permissions import MyPermission
from rest_framework.authentication import SessionAuthentication


class BookViewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
