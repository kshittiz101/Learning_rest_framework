# urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ProfileView,
    BirthCertificateViewSet,
    ApplicationViewSet
)
from django.urls import path, include

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('certificates', BirthCertificateViewSet,
                basename='certificates')
router.register('applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="rest_framework"))
]
