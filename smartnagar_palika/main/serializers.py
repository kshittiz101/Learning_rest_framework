from rest_framework import serializers
from .models import User, Profile, BirthCertificate, Application
from django.utils import timezone


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'date_of_birth', 'address']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'profile']


class BirthCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthCertificate
        fields = [
            'id', 'title', 'date_and_time_of_birth',
            'birth_place', 'father_name', 'mother_name'
        ]


class ApplicationReadSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    approval_by = UserSerializer(read_only=True)
    birth_certificate = BirthCertificateSerializer()

    class Meta:
        model = Application
        fields = [
            'id',
            'applicant',
            'posted_date',
            'approval_by',
            'approval_date',
            'approval_status',
            'remarks',
            'birth_certificate'
        ]


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['birth_certificate']

    def create(self, validated_data):
        user = self.context['request'].user
        return Application.objects.create(applicant=user, **validated_data)


class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['approval_status', 'remarks']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        instance.approval_status = validated_data.get(
            'approval_status', instance.approval_status)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.approval_by = user
        instance.approval_date = timezone.now()
        instance.save()
        return instance
