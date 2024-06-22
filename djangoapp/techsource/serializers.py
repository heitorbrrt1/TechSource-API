from rest_framework import serializers
from django.utils import timezone
from brazilcep import get_address_from_cep
from django.contrib.auth.hashers import make_password

from techsource.Models.usuario import Usuario
from techsource.Models.endereco import Endereco
from techsource.Models.item_pedido import Item_Pedido
from techsource.Models.pedido import Pedido
from techsource.Models.produto import Produto

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

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

    def validate_cep(self, value):
        value = value.replace('-', '').replace('.', '')
        try:
            cep_valido = get_address_from_cep(value)
        except Exception:
            raise serializers.ValidationError("CEP inválido ou não encontrado.")
        
        return value

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        # Se precisar adicionar lógica personalizada na criação do pedido
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Se precisar adicionar lógica personalizada na atualização do pedido
        return super().update(instance, validated_data)

class Item_PedidoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item_Pedido
        fields = '__all__'

    def create(self, validated_data):
        # Se precisar adicionar lógica personalizada na criação do item de pedido
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Se precisar adicionar lógica personalizada na atualização do item de pedido
        return super().update(instance, validated_data)