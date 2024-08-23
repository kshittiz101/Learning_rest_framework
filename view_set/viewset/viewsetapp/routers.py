from rest_framework.routers import DefaultRouter
from .views import BookViewSet
# creating object of default router
router = DefaultRouter()
# register our viewsets
router.register('bookapi',BookViewSet,basename='book')
