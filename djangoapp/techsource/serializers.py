from rest_framework import serializers
from django.utils import timezone
from brazilcep import get_address_from_cep
from django.contrib.auth.hashers import make_password

from techsource.Models.endereco import Endereco
from techsource.Models.item_pedido import Item_Pedido
from techsource.Models.pedido import Pedido
from techsource.Models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Verificar se 'password' está presente nos dados
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

