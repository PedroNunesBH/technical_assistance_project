from django import forms
from .models import Devices


class CreateDevicesForm(forms.ModelForm):

    class Meta:
        model = Devices
        fields = "__all__"
