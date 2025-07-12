from django.utils import timezone
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.authentication import SessionAuthentication

from .models import User, Profile, BirthCertificate, Application
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    BirthCertificateSerializer,
    ApplicationReadSerializer,
    ApplicationCreateSerializer,
    ApplicationStatusUpdateSerializer,
)


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.user_type == "admin":
            return User.objects.all()
        return User.objects.filter(id=user.id)


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class BirthCertificateViewSet(ModelViewSet):
    queryset = BirthCertificate.objects.all()
    serializer_class = BirthCertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Application.objects.all()
        return Application.objects.filter(applicant=user)

    def get_serializer_class(self):
        user = self.request.user

        if self.action == 'create':
            return ApplicationCreateSerializer
        if self.action in ['update', 'partial_update'] and user.user_type == 'admin':
            return ApplicationStatusUpdateSerializer
        return ApplicationReadSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    def perform_update(self, serializer):
        serializer.save(
            approval_by=self.request.user,
            approval_date=timezone.now()
        )
