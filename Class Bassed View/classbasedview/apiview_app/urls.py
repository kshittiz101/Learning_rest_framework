from django.urls import path
from .views import BookListGetOrCreateApi,BookDetailApiView
urlpatterns = [
    path('book/',BookListGetOrCreateApi.as_view(),name='book-create-get'),
    path('book/<int:pk>/',BookDetailApiView.as_view(),name='book-details'),
]
