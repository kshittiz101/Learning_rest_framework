# urls.py
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="author")
router.register("books", BookViewSet, basename="book")


urlpatterns = [
    path("", include(router.urls))
]
