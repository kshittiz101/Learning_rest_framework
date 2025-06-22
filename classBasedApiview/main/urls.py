from django.urls import path
from .views import BookAPIView

urlpatterns = [
    # GET all books, POST new book
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),   # GET one, PUT, DELETE
]
