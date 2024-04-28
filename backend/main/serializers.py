from rest_framework import serializers
from .models import Lembrete

from datetime import date

#métodos create() e update() automáticos
class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ['lembrete_id','nome', 'data']



