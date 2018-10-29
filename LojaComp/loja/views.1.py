'''from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria,Pedido,Pessoa,Produto,Status
from .serializers import CategoriaSerializer, ProdutoSerializer, StatusSerializer, PedidoSerializer, PessoaSerializer
# Create your views here.

class CategoriaViewSet(Categoria):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(Produto):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class StatusViewSet(Status):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class PedidoViewSet(Pedido):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PessoaViewSet(Pessoa):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer'''