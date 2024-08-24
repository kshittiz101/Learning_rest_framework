from django.contrib import admin
from django.urls import path,include
from viewsetapp.routers import router
from modelviewset.routers import router
from readonlymodelviewset.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewset/',include(router.urls)),
    path('modelviewset/',include(router.urls)),
    path('readonlyviewset/',include(router.urls)),
]
