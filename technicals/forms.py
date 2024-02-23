from django.forms import ModelForm
from .models import Technicals


class CreateTechnicalsForm(ModelForm):

    class Meta:
        model = Technicals
        fields = "__all__"
