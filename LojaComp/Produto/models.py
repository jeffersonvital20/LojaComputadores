from django.db import models

# Create your models here.
class Categoria(models.Model):
    objects = models.Manager
    Descricao = models.CharField(max_length=20)
    def __str__(self):
        return self.Descricao


class Produto(models.Model):
    objects = models.Manager
    Nome = models.CharField(max_length=50)
    Quantidade = models.IntegerField(default=0)
    Valor = models.FloatField()
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.Nome
