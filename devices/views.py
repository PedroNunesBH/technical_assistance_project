from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Devices
from .forms import CreateDevicesForm


class HomePage(TemplateView):
    template_name = "base.html"


class ListDevicesView(ListView):
    template_name = "list_devices.html"
    model = Devices


class CreateDevicesView(CreateView):
    template_name = "create_devices.html"
    model = Devices
    form_class = CreateDevicesForm
    success_url = reverse_lazy("list_devices")  # Caso sucesso no formulário redireciona para a url list_devices
