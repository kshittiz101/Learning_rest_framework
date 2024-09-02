from django.contrib import admin
from django.urls import path,include
from api.routers import router


# jwt 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='tokenobtainpair'),
    path('tokenrefresh/',TokenRefreshView.as_view(),name='tokenrefresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='tokenverify'),
]
