from cadastro.models import Anuncio, Categoria
from django.utils import timezone
import random
from django.db.models import Q
from django.contrib.auth.models import User
import random as r


def listify(entrada):
    saida = entrada.split(',')
    comprimento = len(saida)
    saida = saida[:comprimento-1]  # tira o ultimo valor
    return saida


def subtrai_Lists(list1, list2):
    lista = []
    for obj in list1:
        if obj not in list2:
            lista.append(obj)
    return lista


def randomOrdering(objects_list):
    equivalent_number_list = list(range(0, len(objects_list)))
    sorted_number_list = equivalent_number_list.copy()
    r.shuffle(sorted_number_list)
    sorted_objects_list = []
    for i, y in zip(equivalent_number_list, sorted_number_list):
        sorted_objects_list.append(objects_list[y])
    return sorted_objects_list


class ControladorCategorias:
    def __init__(self):
        self.listaCategorias = Categoria.objects.all()

    def __str__(self):
        return print(self.listaCategorias)

    def verificaCategoriasDesteAnuncio(self, Anuncio):
        data_publi = Anuncio.data_publi
        ano_fabricacao = Anuncio.ano_fabricacao
        time_range = timezone.timedelta(days=4)
        lista_categorias_aprovadas = []

        # Anteriores a 1960 - under1960
        if (ano_fabricacao < 2001):
            print('sou menor que 2001')  # --------------------------- debug
            Anuncio.categoria += 'under2001,'
            lista_categorias_aprovadas.append('under2001')
        # Posteriores a 2010 - higher2010
        elif (ano_fabricacao > 2010):
            print('sou maior que 2010')  # --------------------------- debug
            Anuncio.categoria += 'higher2010,'
            lista_categorias_aprovadas.append('higher2010')
        # Entre 2001 e 2010 - 2001to2010
        else:
            print('entre 2001 e 2010')  # --------------------------- debug
            Anuncio.categoria += '2001to2010,'
            lista_categorias_aprovadas.append('2001to2010')

        # else:
        #     if ('under2001' in Anuncio.categoria):
        #         lista_categorias_aprovadas.remove('under2001')

        # # Posteriores a 2010 - higher2010
        # if (ano_fabricacao > 2010):
        #     print('sou maior que 2010')  # --------------------------- debug
        #     Anuncio.categoria += 'higher2010,'
        #     lista_categorias_aprovadas.append('higher2010')
        # else:
        #     if ('higher2010' in Anuncio.categoria):
        #         lista_categorias_aprovadas.remove('higher2010')

        # Publicados recentemente - recently_published
        if (Anuncio.data_publi >= (timezone.now() - timezone.timedelta(days=4))):
            Anuncio.categoria += 'recently_published,'
            lista_categorias_aprovadas.append('recently_published')
        else:
            if ('recently_published' in Anuncio.categoria):
                lista_categorias_aprovadas.remove('recently_published')

        return print(lista_categorias_aprovadas)

    def atualizaListaDeCategorias(self):
        self.listaCategorias = Categoria.objects.all()


class Expositor:
    def __init__(self, Categoria):
        self.categoria = Categoria      # titulo
        self.listaDeAnuncios = []
        self.nome = Categoria.nome
        self.nome_apresentavel = Categoria.nome_apresentavel

    def __str__(self):  # retorna o nome da categoria atribuida ao expositor
        return "Expositor: " + self.categoria.nome

    def addAnuncio(self, Anuncio):
        self.listaDeAnuncios.append(Anuncio)

    @property
    def getAnuncios(self):  # retorna uma lista embaralhada de anuncioa a serem expostos
        return randomOrdering(self.listaDeAnuncios)

    @property
    def getCategoria(self):
        return self.categoria

    @property
    def getNomeCategoria(self):
        return self.categoria.nome

    @property
    def getNomeApresentavelCategoria(self):
        return self.categoria.nome_apresentavel

    def clearExpositor(self):
        self.listaDeAnuncios = []


class ControladorExpositor:
    def __init__(self):
        self.listaAnuncios = Anuncio.objects.all()
        self.lista_categorias = Categoria.objects.all()
        self.lista_expositores = []
        self.anuncioChecked = []
        self.lista_geral_expositores = []

        self.criaExpositores()
        self.preencheExpositores()

# functions  ---------------------------------------------------
    def limpaExpositores(self, lista_expositores):
        for expositor in lista_expositores:
            expositor.clearExpositor()
        return lista_expositores

    def atualizaExpositoresIndex(self):
        self.listaAnuncios = Anuncio.objects.all()
        listUpdate = subtrai_Lists(self.listaAnuncios, self.anuncioChecked)
        if len(listUpdate) > 0:
            for anuncio in listUpdate:
                self.anuncioChecked.append(anuncio)
                for expositor in self.lista_expositores:
                    if expositor.getNomeCategoria in listify(str(anuncio.mem_categorias)):
                        expositor.addAnuncio(anuncio)

# cria  ---------------------------------------------------

    def criaExpositores(self):
        for categoria in self.lista_categorias:
            e = Expositor(categoria)

            # lista que será acessada por todas os tipos de criadores de expositores: Pesquisa, Meus Anuncios e index
            self.lista_expositores.append(e)
            self.lista_geral_expositores.append(e)

            print('------- expositores --------')
            print("-----" + str(e) + "-----")

        self.getNumeroDeExpositores     # retorna o numero de Expositores existentes

# preenche  ---------------------------------------------------

    def preencheExpositores(self, data=None):

        def distribuiAnuncios(anuncios_data, lista_expositores):
            if anuncios_data:
                for anuncio in anuncios_data:
                    for expositor in lista_expositores:
                        # ja tira a categoria recently published
                        if expositor.getNomeCategoria in listify(str(anuncio.mem_categorias)) and expositor.getNomeCategoria != 'recently_published':
                            expositor.addAnuncio(anuncio)
            else:
                print('Sem Anuncios')

        if data:
            # se a informação passada for um user, concluimos que estamos preenchendo uma pagina "Meus Anuncios"
            print(type(data))
            if type(data) != list:
                expositores = self.limpaExpositores(
                    self.lista_expositores)     # retorna a lista ja vazia
                anuncios = Anuncio.objects.filter(anunciante_id=data.id)
                distribuiAnuncios(anuncios, expositores)

            else:   # se não for user, é um resultado de pesquisa
                expositores = self.limpaExpositores(
                    self.lista_expositores)     # retorna a lista ja vazia
                anuncios = data     # equivalente a resultado
                distribuiAnuncios(anuncios, expositores)

        else:
            expositores = self.limpaExpositores(
                self.lista_expositores)  # retorna a lista ja vazia
            anuncios = self.atualizaListaAnuncios
            for anuncio in anuncios:
                # self.anuncioChecked.append(anuncio)
                for expositor in expositores:
                    if expositor.getNomeCategoria in listify(str(anuncio.mem_categorias)):
                        expositor.addAnuncio(anuncio)

# propriedades  ---------------------------------------------------

    @property
    def numeroDeAnunciosNosExpositores(self):
        list = []
        for expositor in self.lista_expositores:
            for anuncio in expositor.getAnuncios:
                list.append(anuncio)
        return len(list)

    @property
    def atualizaListaAnuncios(self):
        self.listaAnuncios = Anuncio.objects.all()
        return self.listaAnuncios

    @property
    def getNumeroDeExpositores(self):
        total = len(self.lista_geral_expositores)
        return print(total)

    @property
    def getListaExpositores(self):
        return self.lista_expositores


class Pesquisador:

    def __init__(self):
        self.lista_categorias = Categoria.objects.all()

    def pesquisaPraMim(self, termos_pesquisados):
        resultados = []
        palavras_chaves = termos_pesquisados.split(' ')
        for palavra in palavras_chaves:

            resultado = Anuncio.objects.filter(
                Q(titulo_anuncio__icontains=palavra) |
                Q(descricao_breve__icontains=palavra) |
                Q(descricao_completa__icontains=palavra) |
                Q(ano_fabricacao__icontains=palavra)
            ).distinct()                        # para nao repetir resultados

            resultados += resultado

        return list(set(resultados))
