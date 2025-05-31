from rest_framework import viewsets
from .models import Categoria, Fornecedor, Produto, LogEntradaSaida
from .serializers import CategoriaSerializer, FornecedorSerializer, ProdutoSerializer, LogEntradaSaidaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class LogViewSet(viewsets.ReadOnlyModelViewSet):  # Apenas leitura
    queryset = LogEntradaSaida.objects.all()
    serializer_class = LogEntradaSaidaSerializer
