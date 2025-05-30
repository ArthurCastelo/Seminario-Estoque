from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProdutoViewSet, SaidaViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'saidas', SaidaViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
