from rest_framework import serializers
from .models import Lembrete

from datetime import date


    

#métodos create() e update() automáticos
class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ['nome', 'data']

    def validate_data(self, data):
        if not data:
            raise serializers.ValidationError("O campo 'data' deverá ser preenchido")
        
        if data < date.today():
            raise serializers.ValidationError("A data não pode estar no passado, deve estar no presente ou no futuro")
        return data


