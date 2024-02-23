from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Technicals
from .forms import CreateTechnicalsForm


class ListTechnicalsView(ListView):
    template_name = "list_technicals.html"
    model = Technicals

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search", "")
        if search:
            queryset = queryset.filter(name__icontains=search)
            return queryset
        return queryset


class CreateTechnicalsView(CreateView):
    template_name = "create_technicals.html"
    model = Technicals
    form_class = CreateTechnicalsForm
    success_url = reverse_lazy("list_technicals")


class UpdateTechnicalsView(UpdateView):
    template_name = "update_technical.html"
    model = Technicals
    form_class = CreateTechnicalsForm
    success_url = reverse_lazy("list_technicals")


class DeleteTechnicalsView(DeleteView):
    template_name = "delete_technical.html"
    model = Technicals
    success_url = reverse_lazy("list_technicals")
