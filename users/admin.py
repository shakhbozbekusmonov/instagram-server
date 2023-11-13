from django.contrib import admin
from .models import User, UserConfirmation


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number']


admin.site.register(UserConfirmation)