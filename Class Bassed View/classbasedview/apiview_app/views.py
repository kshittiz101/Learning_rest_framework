from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import get_object_or_404

class BookListGetOrCreateApi(APIView):
    '''
    handling books and Create list of books
    '''
    def get(self, request, format = None):
        '''
        Querysets
        '''
        books = Book.objects.all()
        serializer = BookSerializer(books,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        '''
        handling post request (create)
        '''
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):
    '''
    handling get, put, patch and  delete for specific book
    '''
    def get(self, request, pk, format = None ):
        book = get_object_or_404(Book,pk =pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format = None):
        book = get_object_or_404(Book, pk =pk)
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errros,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        book = get_object_or_404(Book, pk = pk)
        serializer = BookSerializer(book, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format =None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({'msg':f'Book id={pk} deleted successfully'},status=status.HTTP_204_NO_CONTENT)
