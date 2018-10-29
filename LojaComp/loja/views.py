from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido, Status
from .serializers import PedidoSerializer, StatusSerializer
# Create your views here.
class PedidoViewSet(Pedido):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class StatusViewSet(Status):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

