from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksViewsets, AuthorDetailView, AuthorListView

router = DefaultRouter()
router.register(r'books', BooksViewsets, basename="books")

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('authors/', AuthorListView.as_view(), name="all-author"),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name="authors"),
    path('', include(router.urls)),
]
