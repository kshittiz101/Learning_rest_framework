from django.contrib import admin
from django.urls import path,include
from viewsetapp.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewset/',include(router.urls))
]
