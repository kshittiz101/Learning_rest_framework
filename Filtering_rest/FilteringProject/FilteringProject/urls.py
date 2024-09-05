
from django.contrib import admin
from django.urls import path
from simplefilter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentList.as_view(),name='studentList'),
]
