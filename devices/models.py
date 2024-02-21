from django.db import models


STATUS = [
    ("Em Andamento", "Em Andamento"),
    ("Aguardando Retirada", "Aguardando Retirada"),
    ("Em Orçamento", "Em Orçamento"),
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
    technician = models.CharField(max_length=50)
    problem_description = models.TextField()
