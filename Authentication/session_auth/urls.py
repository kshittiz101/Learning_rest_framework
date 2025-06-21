from django.urls import path, include
from .routers import urlpatterns as router_urls

urlpatterns = [
    path('', include(router_urls)),
    # for browser api we need to include to ask for login and logout
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
