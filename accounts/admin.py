from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import forms
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)




