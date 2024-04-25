from django.db import models

import uuid

#Models para criação das tabelas no modelo relacional

from datetime import date

class Data(models.Model):
    data_id = models.BigIntegerField(primary_key=True, editable=False) 
    data = models.DateField(default=date.today, null=False, blank=False)

    class Meta: 
        db_table = 'data'

    def __str__(self):
        return self.data

class Lembrete(models.Model):
    lembrete_id = models.BigIntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=200, null=False, blank=False, default='null')
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        db_table = 'lembrete'

    def __str__(self):
        return self.nome
    

