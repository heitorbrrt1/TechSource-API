from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    digital = models.BooleanField(default=False, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    # images
    