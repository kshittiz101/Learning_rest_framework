from django.urls import path
from .views import book_detail, book_details

urlpatterns = [
    path('book/<int:pk>/', book_detail, name='book-detail'),
    path('books/', book_details, name='book-details'),
]
