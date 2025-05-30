from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=20)  

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=150)  # Exemplo, pode ser FK se tiver modelo Cliente
    status = models.CharField(max_length=20, default="Pendente")  # Ex: Pendente, Enviado, Cancelado

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

class Entrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada de {self.quantidade} {self.produto.nome} em {self.data}"

class Saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saída de {self.quantidade} {self.produto.nome} em {self.data}"

@receiver(post_save, sender=Produto)
def criar_entrada_automaticamente(sender, instance, created, **kwargs):
    if created:
        Entrada.objects.create(
            produto=instance,
            quantidade=instance.quantidade,
            data=timezone.now()
        )

@receiver(post_delete, sender=Produto)
def registrar_saida_ao_deletar_produto(sender, instance, **kwargs):
    Saida.objects.create(
        produto=instance,
        quantidade=instance.quantidade,
        data=timezone.now()
    )
