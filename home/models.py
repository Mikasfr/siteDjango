from django.db import models

# Create your models here.

class Produtos(models.Model):
    quantidade = models.IntegerField()
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=999999999)
    aplicacao = models.CharField(max_length=999999999)
    valor = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
