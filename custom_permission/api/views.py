from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
from .models import Books
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class AuthorListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class BooksViewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer  # Use BookSerializer here, NOT AuthorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
