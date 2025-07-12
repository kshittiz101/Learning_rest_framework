from django.contrib import admin
from .models import User, Profile, BirthCertificate, Application
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Custom User Admin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )

# Profile Admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address')
    search_fields = ('user__username',)

# Birth Certificate Admin


@admin.register(BirthCertificate)
class BirthCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_and_time_of_birth',
                    'birth_place', 'father_name', 'mother_name')
    search_fields = ('father_name', 'mother_name', 'birth_place')

# Application Admin


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicant', 'approval_status',
                    'approval_by', 'posted_date', 'approval_date')
    list_filter = ('approval_status', 'posted_date')
    search_fields = ('applicant__username', 'birth_certificate__father_name')
