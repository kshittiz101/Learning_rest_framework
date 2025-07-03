from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreationViewsets

router = DefaultRouter()
router.register(r'user', UserCreationViewsets, basename='user')

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
