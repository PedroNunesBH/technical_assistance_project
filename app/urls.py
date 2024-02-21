from django.contrib import admin
from django.urls import path
from devices.views import HomePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage/", HomePage.as_view(), name='homepage')
]
