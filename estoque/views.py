from rest_framework import mixins, viewsets
from .models import Produto, Saida, Pedido
from .serializers import ProdutoSerializer, SaidaSerializer, PedidoSerializer,FornecedorSerializer, EntradaSerializer
import requests
from .models import Fornecedor, Entrada

TELEGRAM_BOT_TOKEN = '7713715877:AAFCoJZCfndfyje_uaEB5zwI_JykxAMuaDk'
TELEGRAM_CHAT_ID = '-4867105687'



class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class EntradaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class SaidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer
    

def notificar_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': msg}
    requests.post(url, data=payload)

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        notificar_telegram(f"✅ Produto {instance.nome} adicionado com sucesso!\n"
                           f"📦 Quantidade: {instance.quantidade}\n"
                           f"💰 Preço unitário: R$ {instance.preco:.2f}\n"
                           f"Obrigado por confiar na gente! 😄")

    def perform_update(self, serializer):
        instance = serializer.save()
        notificar_telegram(f"✅ O Produto *{instance.nome}* foi atualizado com sucesso!\n"
                           f"📦 Quantidade: {instance.quantidade}\n"
                           f"💰 Preço unitário: R$ {instance.preco:.2f}\n")

    def perform_destroy(self, instance):
        notificar_telegram(f"🗑️ Produto *{instance.nome}* foi removido do estoque.\n"
                           f"Se precisar, estamos aqui para ajudar com novos produtos! 😊")
        instance.delete()



class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        pedido = serializer.save()
        msg = f"🛒 Novo pedido criado:\nCliente: {pedido.cliente}\nStatus: {pedido.status}\nItens:\n"
        for item in pedido.itens.all():
            msg += f" - {item.produto.nome}: {item.quantidade}\n"
        notificar_telegram(msg)

    def perform_update(self, serializer):
        pedido = serializer.save()
        notificar_telegram(f"✏️ Pedido {pedido.id} atualizado. Status: {pedido.status}")

    def perform_destroy(self, instance):
        notificar_telegram(f"❌ Pedido {instance.id} do cliente {instance.cliente} foi deletado.")
        instance.delete()
