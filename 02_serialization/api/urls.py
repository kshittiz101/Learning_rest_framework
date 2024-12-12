from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', student_detail, name='student_detail'),
    path('student_details/', student_details, name='student_details'),
    path('single_student/<int:pk>', single_student, name='single_student'),
    path('all_student', all_student, name='all_student'),
]
