
from django.contrib import admin
from django.urls import path,include
from main.routers import router
from sessionauth.routers import router
from custom_per.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('sessionapi/',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('custompermission/',include(router.urls)),
]
