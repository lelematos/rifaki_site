import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    time = timezone.now()
    formato = filename.split('.')[1]
    return 'imagens/carros/anuncio_{0}/{1}'.format(instance.identificador_anuncio, filename)


def removeBlanks(list):
    while("" in list):
        list.remove("")
    return list


class Anuncio(models.Model):
    identificador_anuncio = models.IntegerField()

    TEXT_COLOR_CHOICES = [
        ('black', 'Preto'),
        ('white', 'Branco'),
        ('grey', 'Cinza'),
    ]
    text_color = models.CharField(
        max_length=10,
        choices=TEXT_COLOR_CHOICES,
        default='black',
    )

    titulo_anuncio = models.CharField(max_length=100)

    # marca = models.ChoiceField(choices=c)
    ano_fabricacao = models.IntegerField(default='')

    preco = models.DecimalField(
        max_digits=6, decimal_places=2, default='', error_messages={'invalid': 'Troque a vírgula por ponto!'})

    descricao_breve = models.TextField(max_length=400)
    descricao_completa = models.TextField(max_length=2000)
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE)

    imagem1 = models.ImageField(
        upload_to=user_directory_path, null=False, blank=False, name='imagem1')
    imagem2 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, name='imagem2')
    imagem3 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, name='imagem3')
    imagem4 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, name='imagem4')
    imagem5 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, name='imagem5')

    mem_categorias = models.CharField(max_length=1000, null=True)
    data_publi = models.DateTimeField('data publicação')

    # provavelmente teremos que adicionar ao banco de dados, mas primeiro vamos testar no loop
    categoria = ''

    def __str__(self):
        return self.titulo_anuncio + '  ' + str(self.data_publi)

    @property
    def getListOfImages(self):
        list_images = [str(self.imagem1), str(self.imagem2),
                       str(self.imagem3), str(self.imagem4),
                       str(self.imagem5)
                       ]

        return removeBlanks(list_images)

    @property
    def getFirstImage(self):
        return str(self.imagem1)


class Categoria(models.Model):
    nome = models.CharField(max_length=40)
    nome_apresentavel = models.CharField(max_length=40)
    data_de_criacao = models.DateTimeField()
    index = models.IntegerField(default=0)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Nome da categoria: ' + str(self.nome) + '| Criada por: ' + str(self.criador)
