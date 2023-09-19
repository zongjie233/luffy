from django.contrib import admin
from .models import Banner
from .models import Nav


# Register your models here.
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ["title", "orders", "is_show"]


admin.site.register(Banner, BannerModelAdmin)


class NavModelAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "is_show", "is_site", "position"]


admin.site.register(Nav, NavModelAdmin)

# admin setting site
