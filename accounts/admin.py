from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserType, Language
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 'username',
        'user_type', 'preferred_language', 
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('user_type', 'preferred_language')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('user_type', 'preferred_language')}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(Language)