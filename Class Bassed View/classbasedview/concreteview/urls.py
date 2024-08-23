from django.urls import path
from .views import BookList,BookCreate,BookRetrive,BookUpdate,BookDestory,BookListCreate,BookRetieveUpdate,BookRetriveDestory,RetrieveUpdateDestroyAPIView
urlpatterns = [
    path('booklist/',BookList.as_view(),name='booklist'),
    path('createbook/',BookCreate.as_view(),name='createbook'),
    # path('bookretrieve/<int:pk>/',BookRetrive.as_view(), name='bookretrieve'),
    path('bookupdate/<int:pk>/',BookUpdate.as_view(),name='bookupdate'),
    path('bookdestory /<int:pk>/',BookDestory.as_view(),name='bookdestory'),

    path('booklistcreate/',BookListCreate.as_view(),name='booklistcreate'),
    path('bookretieveupdate/',BookRetieveUpdate.as_view(),name='bookretrieveupdate'),
    path('bookretrivedestory/',BookRetriveDestory.as_view(),name='bookretrivedestory'),
    path('retrieveupdatedestroy/',RetrieveUpdateDestroyAPIView.as_view(),name='retrieveupdatedestroy'),

]
