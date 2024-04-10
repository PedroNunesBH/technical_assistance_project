from django.contrib import admin
from .models import ClientsReviews


class AdminClientsReviews(admin.ModelAdmin):
    list_display = [field.name for field in ClientsReviews._meta.fields]
    search_fields = ("client_name", )


admin.site.register(ClientsReviews, AdminClientsReviews)
