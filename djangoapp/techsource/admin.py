from django.contrib import admin

from techsource.Models.endereco import Endereco
from techsource.Models.item_pedido import Item_Pedido
from techsource.Models.pedido import Pedido
from techsource.Models.produto import Produto
from techsource.Models.usuario import Usuario

admin.site.register(Endereco)
admin.site.register(Item_Pedido)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Usuario)