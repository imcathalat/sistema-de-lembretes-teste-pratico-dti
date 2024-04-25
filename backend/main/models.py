from django.db import models

#Models para criação das tabelas no modelo relacional

from datetime import date

class Lembrete(models.Model):
    nome = models.CharField(max_length=100, null=False)
    data = models.DateField(default=date.today, null=False)

    class Meta:
        db_table = 'lembrete'

    def __str__(self):
        return self.nome

