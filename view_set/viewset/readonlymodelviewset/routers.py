from rest_framework.routers import DefaultRouter
from .views import BookReadOnlyModelViewSet

router = DefaultRouter()
router.register('bookapi',BookReadOnlyModelViewSet,basename='book')