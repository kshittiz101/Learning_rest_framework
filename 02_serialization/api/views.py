from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse


# Create your views here.
def book_detail(request, pk):
    # for model instance
    # creating model instance
    book = Book.objects.get(id=pk)
    # serialization
    # complex to python datatypes
    serializer = BookSerializer(book)
    # convert to json data

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
