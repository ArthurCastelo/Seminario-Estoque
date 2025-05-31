from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProdutoViewSet, SaidaViewSet, PedidoViewSet,EntradaViewSet,FornecedorViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'saidas', SaidaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'entradas', EntradaViewSet)
router.register(r'fornecedores', FornecedorViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
