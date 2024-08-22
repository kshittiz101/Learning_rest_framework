from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''
    List and Create View
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    '''
    Handles GET request to list all books
    '''
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 
    
    '''
    Handles POST request to create a new book
    '''

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 


class BookRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    '''
    Retrieve, Update, and Destroy View
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        '''
        Handles GET request to retrieve a book by its primary key
        '''
        return self.retrieve(request, *args, **kwargs)  

    def put(self, request, *args, **kwargs):
        '''
        Handles PUT request to update an entire book
        '''
        return self.update(request, *args, **kwargs)  
   

    def patch(self, request, *args, **kwargs):
        '''
        Handles PATCH request to partially update a book
        '''
        return self.partial_update(request, *args, **kwargs)  
   

    def delete(self, request, *args, **kwargs):
        '''
        Handles DELETE request to delete a book
        ''' 
        return self.destroy(request, *args, **kwargs)  