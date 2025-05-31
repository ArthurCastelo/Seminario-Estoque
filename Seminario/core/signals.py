from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Produto, LogEntradaSaida
import requests

@receiver(post_save, sender=Produto)
def log_produto_save(sender, instance, created, **kwargs):
    tipo = 'ENTRADA' if created else 'ALTERACAO'
    LogEntradaSaida.objects.create(produto=instance, tipo=tipo, quantidade=instance.quantidade)

@receiver(post_delete, sender=Produto)
def log_produto_delete(sender, instance, **kwargs):
    LogEntradaSaida.objects.create(produto=instance, tipo='SAIDA', quantidade=instance.quantidade)


TOKEN = '7713715877:AAFCoJZCfndfyje_uaEB5zwI_JykxAMuaDk'
CHAT_ID = '-4867105687'  

def enviar_telegram_mensagem(texto):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': texto,
        'parse_mode': 'HTML'
    }
    try:
        requests.get(url, params=payload)
    except Exception as e:
        print("Erro ao enviar mensagem Telegram:", e)


@receiver(post_save, sender=Produto)
def notificar_alteracao_ou_criacao(sender, instance, created, **kwargs):
    if created:
        msg = f"📦 <b>Produto Criado:</b>\nNome: {instance.nome}\nQuantidade: {instance.quantidade}"
    else:
        msg = f"✏️ <b>Produto Atualizado:</b>\nNome: {instance.nome}\nNova Quantidade: {instance.quantidade}"
    enviar_telegram_mensagem(msg)


@receiver(post_delete, sender=Produto)
def notificar_exclusao(sender, instance, **kwargs):
    msg = f"❌ <b>Produto Removido:</b>\nNome: {instance.nome}"
    enviar_telegram_mensagem(msg)
