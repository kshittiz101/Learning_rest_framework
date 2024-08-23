
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('apiview/',include('apiview_app.urls')),
    path('generic/',include('genericAndmixin.urls')),
    path('concreteview/',include('concreteview.urls')),
]
