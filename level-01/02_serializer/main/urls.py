from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewsets
router = DefaultRouter()
router.register("books", BookViewsets, basename="books")

urlpatterns = [
    path('', include(router.urls))
]
