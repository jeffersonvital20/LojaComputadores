from django.db import models
from Pessoa.models import Pessoa

# Create your models here.
class Status(models.Model):
    objects = models.Manager
    Situacao = models.CharField(max_length=30)
    Descricao = models.CharField(max_length=30)
    def __str__(self):
        return self.Situacao


class Pedido(models.Model):
    objects = models.Manager
    Numero = models.IntegerField(default=0)
    Cliente = models.ManyToManyField(Pessoa, null=True,blank=True)
    Status = models.ManyToManyField(Status, null=True,blank=True)
    #Produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(str(self.pk), str(self.Numero))

    