from django.urls import path
from api.views import BookViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('books', BookViewsets, basename='books')

urlpatterns = [

]
urlpatterns += router.urls
