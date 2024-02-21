from django.contrib import admin
from .models import Devices


class DevicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Devices._meta.fields]
    search_fields = ("model", "name")


admin.site.register(Devices, DevicesAdmin)
