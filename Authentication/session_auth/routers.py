from rest_framework.routers import DefaultRouter
from .views import BooksViewsets

router = DefaultRouter()
router.register('books', BooksViewsets, basename='books')

urlpatterns = router.urls
