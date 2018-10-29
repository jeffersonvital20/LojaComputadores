from rest_framework.serializers import  ModelSerializer
from Produto.models import Produto, Categoria

# Serializers define the API representation.
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id','Nome','Quantidade','Valor','Categoria')


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','Descricao')