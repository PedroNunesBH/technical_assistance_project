from django.contrib import admin
from .models import Technicals


class TechnicalsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Technicals._meta.fields]
    search_fields = ("name", "id")


admin.site.register(Technicals, TechnicalsAdmin)
