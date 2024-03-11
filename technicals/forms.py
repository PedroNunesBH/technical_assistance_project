from django.forms import ModelForm
from .models import Technicals


class CreateTechnicalsForm(ModelForm):

    class Meta:
        model = Technicals
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateTechnicalsForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["cpf"].label = "CPF"
        self.fields["admission_date"].label = "Data de Admissão"
        self.fields["salary"].label = "Salário"
        self.fields["phone_number"].label = "Número de Telefone"
