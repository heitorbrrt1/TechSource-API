from django.db import models
from .usuario import Usuario

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    id_transacao = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)