from django.shortcuts import render
from .serializers import StudentSerializer
from  .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
# for search we don't need Post, put, patch and delete, we only need list 
# so we will only create list 

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # using get_queryset() --> function, this applicable for only for user who create api and want to see 
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(pass_by = user)
