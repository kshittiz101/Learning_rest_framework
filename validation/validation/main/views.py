from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_api(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data = python_data)
    if serializer.is_valid():
        serializer.save()
        response = {'msg':'Data is inseted successfully'}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type = 'application/json')


