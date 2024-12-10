from rest_framework import serializers
from clientes.models import Cliente
from .validacao import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError("CPF Invalido")
        if not nome_valido(data['nome']):
            raise serializers.ValidationError("Não inclua numeros")
        if not rg_valido(data['rg']):
            raise serializers.ValidationError("RG deve ter 9 digitos")
        if not celular_valido(data['celular']):
            raise serializers.ValidationError("O número deve seguir este modelo 47 91234-1234")

        return data