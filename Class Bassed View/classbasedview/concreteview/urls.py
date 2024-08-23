from django.urls import path
from .views import BookList,BookCreate
urlpatterns = [
    path('booklist/',BookList.as_view(),name='booklist'),
    path('createbook/',BookCreate.as_view(),name='createbook'),
]
