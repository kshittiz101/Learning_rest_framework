from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # internally in classes 
    # if we have more than one classes required same permission then we do 
    # global permission
    # that is done in setting.py file
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
