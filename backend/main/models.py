from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


import uuid

#Models para criação das tabelas no modelo relacional
from datetime import datetime
from datetime import date

def validar_data_no_presente_ou_futuro(value):
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError(_('Formato de data inválido'))
    
    if value < date.today():
        raise ValidationError(_('A data não pode estar no passado, deve estar no presente ou no futuro'))


class Lembrete(models.Model):
    lembrete_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    data = models.DateField(null=False, blank=False, default=date.today, validators=[validar_data_no_presente_ou_futuro])
    
    class Meta:
        db_table = 'lembrete'

    def __str__(self):
        return f"Lembrete: {self.nome}."
    

