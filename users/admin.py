from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    pass
