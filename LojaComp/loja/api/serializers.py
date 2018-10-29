from rest_framework.serializers import  ModelSerializer
from loja.models import Pedido, Status
from Pessoa.api.serializers import PessoaSerializer
from rest_framework.fields import SerializerMethodField

# Serializers define the API representation.
class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('Situacao','Descricao')


class PedidoSerializer(ModelSerializer):
    Cliente = PessoaSerializer(many=True)
    Status = StatusSerializer(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ('id','Numero','Cliente','Status','descricao_completa')

    def get_descricao_completa(self,obj):
        return '{} - {} - {}'.format(str(obj.Numero),obj.Cliente,obj.Status)
