from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound

# Exempt CSRF for testing with tools like Postman, remove in production
@csrf_exempt 
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        if json_data:
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                except Student.DoesNotExist:
                    return JsonResponse({'error': 'Student not found'}, status=404)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data, safe=False)
        
        # If no ID is provided, return all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'msg':'data inserted sucessfully'
            }
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type = 'application/json')
        
        # if not valid
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        # partial update 
        serializer = StudentSerializer(stu, data = python_data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'data updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {'msg':'Data is Deleted !!!'}
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(response, safe=False)


    # Optionally handle other HTTP methods like POST, PUT, DELETE
    return HttpResponse(status=405)  # Method not allowed
