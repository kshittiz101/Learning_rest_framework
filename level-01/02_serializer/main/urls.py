from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewsets, SnippetViewsets
router = DefaultRouter()
router.register("books", BookViewsets, basename="books")
router.register("snippet", SnippetViewsets, basename="snippet")

urlpatterns = [
    path('', include(router.urls))
]
