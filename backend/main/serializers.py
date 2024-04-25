from rest_framework import serializers
from .models import Lembrete

#métodos create() e update() automáticos
class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ['nome', 'data']

    def validate_data(self, data):
        if not data:
            raise serializers.ValidationError("O campo 'nome' e 'data' deverá ser preenchido")
        return data
