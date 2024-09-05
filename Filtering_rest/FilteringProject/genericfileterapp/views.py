from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

# Local application of django-filters for Student model
class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  # Correct field name for filtering