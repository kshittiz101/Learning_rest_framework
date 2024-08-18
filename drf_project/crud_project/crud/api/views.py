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
        # Fetch all student records from the database
        students = Student.objects.all()
        # Serialize the data convert inot python native types
        serializer = StudentSerializer(students, many=True)
        # Return the serialized data as a JSON response
        return JsonResponse(serializer.data, safe=False)
    
    
            
                    

            
