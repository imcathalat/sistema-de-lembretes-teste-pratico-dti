from rest_framework import serializers
from .models import Lembrete, Data

from datetime import date

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['data']

    def validate_data(self, data):
        if not data:
            raise serializers.ValidationError("O campo 'nome' e 'data' deverá ser preenchido")
        
        if data < date.today:
            raise serializers.ValidationError("A data não pode estar no passado, deve estar no presente ou no futuro")
        return data

#métodos create() e update() automáticos
class LembreteSerializer(serializers.ModelSerializer):
    data = DataSerializer()

    class Meta:
        model = Lembrete
        fields = ['nome', 'data']

    def create(self, validated_data):
        data_validated = validated_data.pop('data')
        nova_data = Data.objects.create(**data_validated)
        lembrete = Lembrete.objects.create(data=nova_data, **validated_data)
        return lembrete


