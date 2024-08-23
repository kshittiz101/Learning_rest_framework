from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class BookList(ListAPIView):
    '''
    handle book list
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrive(RetrieveAPIView):
    '''
    Retrive specific book
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(CreateAPIView):
    '''
    Create book
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdate(UpdateAPIView):
    '''
    update book
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDestory(DestroyAPIView):
    '''
    Destory book or delete book
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# mixing one and two values
class BookListCreate(ListCreateAPIView):
    '''
    this class handle get and post method handler
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetieveUpdate(RetrieveUpdateAPIView):
    '''
    this class handle Put,patch and get
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetriveDestory(RetrieveDestroyAPIView):
    '''
    this class retrieve, delete (get and Delete)
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''
    This class get,put, patch and delete
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

