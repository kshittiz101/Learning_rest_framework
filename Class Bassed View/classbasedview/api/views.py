
# function based api view

from .serializers import BookSerializer
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def book_create_or_get(request):
    if request.method == 'GET':
        # query sets
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'sucess':'Book added successfully '},status=status.HTTP_201_CREATED)
        return Response({'error':'Invalid data'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book_detail(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)
    
    # handling GET method 
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Book is updated successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({'sucess':'Deleted Successfully'},status=status.HTTP_200_OK)


