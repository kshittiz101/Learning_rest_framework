from rest_framework.routers import DefaultRouter
from .views import StudentModelViewset

router = DefaultRouter()
router.register('studentapi',StudentModelViewset,basename='students')