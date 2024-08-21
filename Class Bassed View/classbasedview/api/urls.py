from django.urls import path
from .views import book_create_or_get,book_detail
urlpatterns = [
    path('book_create_or_get/',book_create_or_get,name='book_create_or_get'),
    path('book_detail/<int:pk>/',book_detail, name='book_detail'),
]
