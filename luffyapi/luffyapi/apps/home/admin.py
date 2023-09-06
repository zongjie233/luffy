from django.contrib import admin
from .models import Banner


# Register your models here.
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ["title", "orders", "is_show"]


admin.site.register(Banner, BannerModelAdmin)

# admin setting site
