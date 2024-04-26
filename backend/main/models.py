from django.db import models

import uuid

#Models para criação das tabelas no modelo relacional
from datetime import datetime
from datetime import date

class Data(models.Model):
    data_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    data = models.DateField(default=date.today, null=False, blank=False)

    class Meta: 
        db_table = 'data'
        ordering = ('-data',)

    def __str__(self):
        # formatação da data para estilo brasileiro (dd/mm/yyyy)
        data_formatada = self.data.strftime('%d/%m/%Y')
        return f"data {self.data}"

class Lembrete(models.Model):
    lembrete_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        db_table = 'lembrete'

    def __str__(self):
        return self.nome
    

