from django.contrib import admin
from django.urls import path
from simplefilter import views as simplefilter_views
from genericfileterapp import views as genericfilter_views
from searchfilterapp import views as genericserach_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', simplefilter_views.StudentList.as_view(), name='studentList'),
    path('studentlistapi/', genericfilter_views.StudentListApi.as_view(), name='studentlistapi'),
    path('studentsearchapi/', genericserach_views.StudentGenericApi.as_view(), name='studentsearchapi'),
]