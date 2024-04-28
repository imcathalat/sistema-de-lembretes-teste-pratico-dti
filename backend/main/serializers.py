from rest_framework import serializers
from .models import Lembrete

from datetime import date

#métodos create() e update() automáticos
class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ['lembrete_id','nome', 'data']

    # def validate_data(self, value):
    #     if not value:
    #         raise serializers.ValidationError("O campo 'data' deverá ser preenchido")

    #     if value >= date.today():
    #         raise serializers.ValidationError("A data não pode estar no passado, deve estar no presente ou no futuro")
    #     return value



