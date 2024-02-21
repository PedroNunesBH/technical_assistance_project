from django.contrib import admin
from django.urls import path
from devices.views import HomePage, ListDevicesView, CreateDevicesView, UpdateDeviceView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("homepage/", HomePage.as_view(), name='homepage'),
    path("list_devices/", ListDevicesView.as_view(), name='list_devices'),
    path("create_devices/", CreateDevicesView.as_view(), name='create_devices'),
    path("update_device/<int:pk>", UpdateDeviceView.as_view(), name='update_device')
]
