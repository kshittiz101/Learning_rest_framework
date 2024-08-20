from django.urls import path
from .views import *
urlpatterns = [
    path('book_get_or_create/',book_get_or_create,name='book_get_or_create'),
    path('book_detail/<int:pk>/',book_detail,name='book_detail'),
]
