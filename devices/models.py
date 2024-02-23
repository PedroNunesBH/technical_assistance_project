from django.db import models
from technicals.models import Technicals


STATUS = [
    ("Aguardando Aprovação", "Aguardando Aprovação"),
    ("Em Andamento", "Em Andamento"),
    ("Aguardando Retirada", "Aguardando Retirada"),
    ("Em Orçamento", "Em Orçamento"),
    ("Entregue", "Entregue ao Cliente")
]


class Devices(models.Model):
    model = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=30)
    client_email = models.EmailField()
    entry_date = models.DateTimeField(
        auto_now_add=True
    )  # Adiciona automaticamente data e hora de entrada do aparelho
    status = models.CharField(choices=STATUS, max_length=50)
    repair_price = models.CharField(default="Aguardando Orçamento", max_length=100)
    technician = models.ForeignKey(Technicals, on_delete=models.PROTECT, related_name='devices_technicals')
    problem_description = models.TextField()
