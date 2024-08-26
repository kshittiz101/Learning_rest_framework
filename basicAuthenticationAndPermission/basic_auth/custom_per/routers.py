from rest_framework.routers import DefaultRouter
from .views import BookModelViewset

router = DefaultRouter()
router.register('booksapi',BookModelViewset,basename='books')