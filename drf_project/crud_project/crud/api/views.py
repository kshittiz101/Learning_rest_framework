from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student 
from django.http import JsonResponse

# Create your views here.
# get all student
def student_api(request):
    if request.method == 'GET':
        student_id = request.GET.get('id')
        if student_id is not None:
            try:
                #fetch the student with given id 
                student = Student.objects.get(id=student_id)
                # serialize data 
                serializer = StudentSerializer(student)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error':'Student not found'},status = 404)
        

        # Fetch all student records from the database
        students = Student.objects.all()
        # Serialize the data convert inot python native types
        serializer = StudentSerializer(students, many=True)
        # Return the serialized data as a JSON response
        return JsonResponse(serializer.data, safe=False)
    
    
            
                    

            
