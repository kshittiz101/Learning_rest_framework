from django.urls import path
from .views import book_api
urlpatterns = [
    path('book_api/',book_api,name='book_api'),
]
