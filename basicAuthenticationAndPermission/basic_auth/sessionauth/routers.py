from rest_framework.routers import DefaultRouter
from .views import BookModelViewSet

router = DefaultRouter()
router.register('books',BookModelViewSet,basename='books')