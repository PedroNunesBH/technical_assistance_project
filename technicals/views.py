from django.views.generic import ListView
from .models import Technicals


class ListTechnicalsView(ListView):
    template_name = "list_technicals.html"
    model = Technicals
