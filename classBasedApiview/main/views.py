from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Books
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework import status


class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Books, pk=pk)
            serializer = BooksSerializer(book)
            return Response(serializer.data)
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
