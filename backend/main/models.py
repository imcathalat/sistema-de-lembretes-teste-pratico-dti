from django.db import models

import uuid

#Models para criação das tabelas no modelo relacional
from datetime import datetime
from datetime import date

class Lembrete(models.Model):
    lembrete_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    
    class Meta:
        db_table = 'lembrete'

    def __str__(self):
        return f"Lembrete: {self.nome}."
    

