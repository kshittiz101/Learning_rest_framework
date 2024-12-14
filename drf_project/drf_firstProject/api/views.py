from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer

# Create your views here.

# model instance


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)  # model instance i.e. complex data
    serializer = StudentSerializer(stu)  # convert into python native datatypes
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    return HttpResponse(json_data, content_type='application/json')


# querysets
def student_detalis(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# using JSONResponse
def single_student(request,pk):
    try:
        stu = Student.objects.get(id = pk)
    # serializer = StudentSerializer()
    except Student.DoesNotExist:
        return JsonResponse({'error':'Student not found'},status = 404)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)


def all_student(request):
    # query sets
    try: 
        stu= Student.objects.all()
    except Student.DoesNotExist:
        return JsonResponse({'error':'Student not found'},status = 404)
    serializer = StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)