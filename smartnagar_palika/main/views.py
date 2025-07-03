
from .serializers import UserSerializer
from .models import User, Profile
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

# Create your views here.


class UserCreationViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
