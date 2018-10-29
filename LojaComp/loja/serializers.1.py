'''from rest_framework import  serializers
from .models import Categoria,Pedido,Pessoa,Produto,Status

# Serializers define the API representation.
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('Descricao')


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('Nome','Quantidade','Valor','Categoria_id')





class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('Numero','Status','Produto_id')


'''