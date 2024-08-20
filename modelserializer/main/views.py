from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def book_api(request):
    if request.method == 'GET':
        # querysets
        books = Book.objects.all()
        # python data convert
        serializer = BookSerializer(books,many=True)
        # jsondata
        json_data = JSONRenderer().render(serializer.data)
        # return response
        return HttpResponse(json_data,content_type ='application/json')
        
