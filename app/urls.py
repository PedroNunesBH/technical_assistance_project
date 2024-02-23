from django.contrib import admin
from django.urls import path
from devices.views import (HomePage, ListDevicesView, CreateDevicesView, UpdateDeviceView,
                           DeleteDeviceView)
from technicals.views import (ListTechnicalsView, CreateTechnicalsView, UpdateTechnicalsView,
                              DeleteTechnicalsView)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("homepage/", HomePage.as_view(), name='homepage'),
    path("list_devices/", ListDevicesView.as_view(), name='list_devices'),
    path("create_devices/", CreateDevicesView.as_view(), name='create_devices'),
    path("update_device/<int:pk>", UpdateDeviceView.as_view(), name='update_device'),
    path("delete_device/<int:pk>", DeleteDeviceView.as_view(), name='delete_device'),

    path("list_technicals/", ListTechnicalsView.as_view(), name='list_technicals'),
    path("create_technicals/", CreateTechnicalsView.as_view(), name='create_technicals'),
    path("update_technical/<int:pk>", UpdateTechnicalsView.as_view(), name='update_technical'),
    path("delete_technical/<int:pk>", DeleteTechnicalsView.as_view(), name='delete_technical')
]
