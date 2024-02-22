from django.db import models


class Technicals(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    admission_date = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return self.name
