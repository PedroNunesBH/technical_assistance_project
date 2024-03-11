from django import forms
from .models import Devices


class CreateDevicesForm(forms.ModelForm):

    class Meta:
        model = Devices
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateDevicesForm, self).__init__(*args, **kwargs)
        self.fields["model"].label = "Modelo"
        self.fields["client_name"].label = "Nome do Cliente"
        self.fields["client_phone"].label = "Telefone do Cliente"
        self.fields["client_email"].label = "Email do Cliente"
        self.fields["repair_price"].label = "Preço do Conserto"
        self.fields["technician"].label = "Técnico Responsável"
        self.fields["problem_description"].label = "Descrição do Problema"
