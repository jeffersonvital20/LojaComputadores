from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from loja.models import Pedido, Status
from .serializers import PedidoSerializer, StatusSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class StatusViewSet(ModelViewSet):
    #queryset = Status.objects.all()
    serializer_class = StatusSerializer
    def queryset(self):
        return Status.objects.all()


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends =(DjangoFilterBackend, SearchFilter)
    search_fields = ('^status__situacao')
    filter_fields = ('id','Numero')

    # def queryset(self):
    #     id = self.request.query_params.get('id', None)
    #     #Numero = self.request.query_params.GET('Numero',None)
    #     queryset =  Pedido.objects.all()
    #     if id:
    #         queryset = Pedido.objects.filter(pk=id)
    #         print(str(id))
        
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     return super Pedido
    @action(methods=['GET'], detail=True)
    def VisualizarPedido(self, request, pk=id): #Pedido.Cliente.Tipo = 'admin'):
        pass