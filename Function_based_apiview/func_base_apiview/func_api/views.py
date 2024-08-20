from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET','POST'])
def book_get_or_create(request):
    # this code for get method
    if request.method == 'GET':
        # id = request.GET.get('id',None)
        # if id is not None:
        #     # for single value 
        #     book = Book.objects.get(id = id)
        #     serializer = BookSerializer(book)
        #     return Response(serializer.data,status=status.HTTP_200_OK)
        
        # query set
        books = Book.objects.all()
        # serialize data
        serializer = BookSerializer(books,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def book_detail(request,pk):
    # get book from database
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)
    # handling get method 
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # handling post method 
    if request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # handling delete method 
    if request.method == 'DELETE':
        book.delete()
        return Response({'msg':'Delete successfully'},status=status.HTTP_204_NO_CONTENT)


