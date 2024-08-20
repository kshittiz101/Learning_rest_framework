from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
def book_api(request):
    if request.method == 'GET':
        # get book id from request object
        id = request.GET.get('id',None)
        if id is not None:
            try:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,content_type='application/json')
            except Book.DoesNotExist():
                return JsonResponse({'error': 'Book not found'}, status=404)
        else:
            # querysets
            books = Book.objects.all()
            # python data convert
            serializer = BookSerializer(books,many=True)
            # jsondata
            json_data = JSONRenderer().render(serializer.data)
            # return response
            return HttpResponse(json_data,content_type ='application/json')

