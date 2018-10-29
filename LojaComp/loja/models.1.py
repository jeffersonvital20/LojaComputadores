'''from django.db import models

# Create your models here.
class Categoria(models.Model):
    objects = models.Manager
    Descricao = models.CharField(max_length=20)
    def __str__(self):
        return self.Descricao


class Produto(models.Model):
    objects = models.Manager
    Nome = models.CharField(max_length=50)
    Quantidade = models.IntegerField()
    Valor = models.FloatField()
    Categoria_id = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    def __str__(self):
        return self.Nome





class Pedido(models.Model):
    objects = models.Manager
    Numero = models.IntegerField()
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.Numero

class Pessoa(models.Model):
    objects = models.Manager
    Nome = models.CharField(max_length=50)
    Senha = models.CharField(max_length=50)
    Endereco =  models.CharField(max_length=50)
    Tipo = models.CharField(max_length=20)
    Pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)'''

    