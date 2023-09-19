from django.contrib import admin

from .models import User


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_staff", "is_active"]


admin.site.register(User, UserModelAdmin)
