from rest_framework import serializers
from .models import Produto,ItemPedido,Pedido,Saida

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)  # Para lidar com os itens embutidos

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido

    def update(self, instance, validated_data):
        itens_data = validated_data.pop('itens', None)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if itens_data is not None:
            # Atualiza os itens: para simplificar, exclui e cria novamente
            instance.itens.all().delete()
            for item_data in itens_data:
                ItemPedido.objects.create(pedido=instance, **item_data)

        return instance

