from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Devices


class HomePage(TemplateView):
    template_name = "base.html"


class ListDevicesView(ListView):
    template_name = "list_devices.html"
    model = Devices
