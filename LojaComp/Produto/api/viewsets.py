from rest_framework.viewsets import ModelViewSet
from Produto.models import Produto , Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework.authentication import TokenAuthentication

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    filter_backends =(DjangoFilterBackend, SearchFilter)
    search_fields = ('^Nome')
    filter_fields = ('id','Nome')

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer