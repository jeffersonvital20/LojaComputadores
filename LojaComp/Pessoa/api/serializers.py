from rest_framework.serializers import  ModelSerializer
from Pessoa.models import Pessoa

# Serializers define the API representation.
class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','Nome','Endereco','Tipo','Foto')
