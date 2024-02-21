from django.contrib import admin
from django.urls import path
from devices.views import HomePage, ListDevicesView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage/", HomePage.as_view(), name='homepage'),
    path("all_devices/", ListDevicesView.as_view(), name='list_devices')
]
