from django.urls import path, include
from api.views import BookViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('books', BookViewsets, basename='books')

urlpatterns = [
    # for browser api we need to include to ask for login and logout
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += router.urls
