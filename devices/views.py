from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Devices
from .forms import CreateDevicesForm


class ListDevicesView(LoginRequiredMixin, ListView):
    template_name = "list_devices.html"
    model = Devices

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(client_name__icontains=search)
        return queryset


class CreateDevicesView(LoginRequiredMixin, CreateView):
    template_name = "create_devices.html"
    model = Devices
    form_class = CreateDevicesForm
    success_url = reverse_lazy("list_devices")  # Caso sucesso no formulário redireciona para a url list_devices


class UpdateDeviceView(LoginRequiredMixin, UpdateView):
    template_name = "update_device.html"
    model = Devices
    form_class = CreateDevicesForm
    success_url = reverse_lazy('list_devices')


class DeleteDeviceView(LoginRequiredMixin, DeleteView):
    template_name = "delete_device.html"
    model = Devices
    success_url = reverse_lazy("list_devices")
