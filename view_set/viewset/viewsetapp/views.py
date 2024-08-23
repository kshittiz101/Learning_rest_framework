from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ViewSet):
    def list(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    # id required
    def retrieve(self, request,pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def update(self,request,pk=None):
        '''
        updating book data in specific id
        complete data update
        '''
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'Unable to update'},status=status.HTTP_400_BAD_REQUEST)

        

    def partial_update(self,request, pk=None):
        '''
        partially updating value of the book
        '''
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'Book Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'Unable to update'},status=status.HTTP_400_BAD_REQUEST)

        

    def destory(self, request,pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'Book Not found'})
        book.delete()
        return Response({'msg':'delete successfully'},status=status.HTTP_204_NO_CONTENT)

