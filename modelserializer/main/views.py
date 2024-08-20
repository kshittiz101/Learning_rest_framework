from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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
        
    if request.method == 'POST':
        # Get the incoming JSON data
        json_data = request.body
        # Convert the JSON data into a stream
        stream = io.BytesIO(json_data)
        # Parse the stream into Python data
        python_data = JSONParser().parse(stream)
        # Pass the Python data to the serializer
        serializer = BookSerializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data has been inserted successfully'}, status=201)
        
        # If the data is not valid
        return JsonResponse(serializer.errors, status=400)
