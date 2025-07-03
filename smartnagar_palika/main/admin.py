from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'user_type', 'is_staff', 'get_date_of_birth', 'get_address'
    )

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )

    def get_date_of_birth(self, obj):
        return obj.profile.date_of_birth if hasattr(obj, 'profile') else '-'
    get_date_of_birth.short_description = 'Date of Birth'

    def get_address(self, obj):
        return obj.profile.address if hasattr(obj, 'profile') else '-'
    get_address.short_description = 'Address'
