from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True)
    preco = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    descricao = models.TextField(null=True, blank=True)
    capa = models.ImageField(null=True, blank=True)
    midias = models.ManyToManyField(Midia, related_name='produtos')
