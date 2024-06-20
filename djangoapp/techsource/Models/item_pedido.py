from django.db import models
from .produto import Produto
from .pedido import Pedido

class Item_Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_item = models.DateTimeField(auto_now_add=True)
