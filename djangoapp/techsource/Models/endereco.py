from django.core.validators import RegexValidator
from django.db import models
from .usuario import Usuario
from .pedido import Pedido

class Endereco(models.Model):
    UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)

    cidade = models.CharField(max_length=30, null=True)
    estado = models.CharField(choices=UF_CHOICES,max_length=32, blank=False, null=False)
    
    rua = models.CharField(null=False, blank=False)
    bairro = models.CharField(null=False, blank=False)
    numero = models.CharField(null=False, blank=False, max_length=16384)
    cep = models.CharField(max_length=9, validators=[RegexValidator(regex=r'^\d{5}-\d{3}$', message='CEP inválido.')], null=False, blank=False)
    complemento = models.CharField(max_length=30, null=True, blank=True)
