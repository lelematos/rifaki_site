from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Anuncio


class NumeroDaSorte(models.Model):
    numero_escolhido = models.IntegerField()
    anuncio_escolhido = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    comprador = models.ForeignKey(
        User, on_delete=models.CASCADE)


class Carrinho(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_ultima_modificacao = models.DateTimeField()
    itens = models.ManyToManyField(NumeroDaSorte)


class Venda(models.Model):
    comprador_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comprador')
    vendedor_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='vendedor')
    data_de_registro = models.DateTimeField()
    numero_vendido = models.ForeignKey(NumeroDaSorte, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=8)
