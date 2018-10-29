from django.db import models

# Create your models here.
class Pessoa(models.Model):
    objects = models.Manager
    Nome = models.CharField(max_length=50)
    Senha = models.CharField(max_length=50)
    Endereco =  models.CharField(max_length=50)
    Tipo = models.CharField(max_length=20)
    Foto = models.ImageField(upload_to="FotosClientes",null=True, blank=True)
    #Pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.Nome,self.Tipo)