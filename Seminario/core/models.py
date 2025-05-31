from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class LogEntradaSaida(models.Model):
    TIPO_CHOICES=[
        ('ENTRADA','Entrada'),
        ('SAIDA','Saída'),
        ('Alteração','ALTERACAO')
    ]

    produto=models.ForeignKey(Produto,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10,choices=TIPO_CHOICES)
    quantidade =models.IntegerField(null=True,blank=True)
    data =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo}" - {self.produto.nome}