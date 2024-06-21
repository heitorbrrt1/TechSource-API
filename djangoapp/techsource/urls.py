from django.urls import path, include
from rest_framework.routers import DefaultRouter
from techsource.views import index, UsuarioViewSet

app_name = 'techsource'

# Crie um roteador e registre o UsuarioViewSet
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),  # Inclui as rotas do viewset sob a rota 'api/'
]
