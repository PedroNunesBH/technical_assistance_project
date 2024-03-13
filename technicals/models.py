from django.db import models

EMPLOYEES_POSITIONS = [
    ("Atendente", "Atendente"),
    ("Gerente", "Gerente"),
    ("Técnico", "Técnico")
]


class Technicals(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    admission_date = models.DateField()
    salary = models.FloatField()
    employee_position = models.CharField(choices=EMPLOYEES_POSITIONS, max_length=100)
    phone_number = models.CharField(default="Não Informado", max_length=20)

    def __str__(self):
        return self.name
