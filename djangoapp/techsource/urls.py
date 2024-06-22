from django.urls import path, include
from rest_framework.routers import DefaultRouter
from techsource.views import index, UsuarioViewSet, EnderecoViewSet, Item_PedidoViewSet, PedidoViewSet, ProdutoViewSet

app_name = 'techsource'

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'enderecos', EnderecoViewSet, basename='endereco')
router.register(r'item_pedidos', Item_PedidoViewSet, basename='item_pedido')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),  # Inclui as rotas do viewset sob a rota 'api/'
]
