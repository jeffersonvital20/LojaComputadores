from django.views import generic
from django.shortcuts import render
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaView(generic.DetailView):
    model = Pessoa
    template_name = 'base.html'