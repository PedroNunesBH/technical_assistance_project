from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Technicals
from .forms import CreateTechnicalsForm
from .mixins import OnlyAdminMixin


class ListTechnicalsView(LoginRequiredMixin, OnlyAdminMixin, ListView):
    template_name = "list_technicals.html"
    model = Technicals

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")
        if search:
            queryset = queryset.filter(name__icontains=search)
            return queryset
        return queryset


class CreateTechnicalsView(LoginRequiredMixin, OnlyAdminMixin, CreateView):
    template_name = "create_technicals.html"
    model = Technicals
    form_class = CreateTechnicalsForm
    success_url = reverse_lazy("list_technicals")


class UpdateTechnicalsView(LoginRequiredMixin, OnlyAdminMixin, UpdateView):
    template_name = "update_technical.html"
    model = Technicals
    form_class = CreateTechnicalsForm
    success_url = reverse_lazy("list_technicals")


class DeleteTechnicalsView(LoginRequiredMixin, OnlyAdminMixin, DeleteView):
    template_name = "delete_technical.html"
    model = Technicals
    success_url = reverse_lazy("list_technicals")


class OnlyAdminErrorView(TemplateView):  # View que para exibir template de restrição de admin
    template_name = "only_admin.html"
