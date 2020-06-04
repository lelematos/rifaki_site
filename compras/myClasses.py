from cadastro.models import Anuncio
from .models import NumeroDaSorte


def subtrai_Lists(list1, list2):
    lista = []
    for obj in list1:
        if obj not in list2:
            lista.append(obj)
    return lista


class ControladorDeCompras:

    def __init__(self):
        self.numero_de_vendidos = 0
        self.numero_de_restantes = 0
        self.valor_arrecadado = 0
        self.lista_numeros_restantes = []
        self.lista_numeros_vendidos = []
        self.numeros_no_carrinho = []
        self.numeros_vendidos = []

    def getTheNumbersOfAnuncio(self, anuncio):
        self.numeros_no_carrinho = NumeroDaSorte.objects.filter(
            anuncio_escolhido=anuncio)

        # ainda precisa implementar a venda
        # self.numero_de_vendidos = Vendas.objects.filter(
        #     anuncio_escolhido=anuncio)

        # por enquanto vai ser numeros no_carrinho, mas na vdd vamos usar o numeros vendidos
        self.numero_de_vendidos = len(self.numeros_no_carrinho)
        self.numero_de_restantes = 1000-self.numero_de_vendidos

        self.valor_arrecadado = self.numero_de_vendidos*anuncio.preco

        for numero in self.numeros_no_carrinho:
            self.lista_numeros_vendidos.append(numero.numero_escolhido)

        self.lista_numeros_restantes = subtrai_Lists(
            list(range(0, 1000)), self.lista_numeros_vendidos)

    @property
    def getNumeroDeVendidos(self):
        # por enquanto vai ser numeros no_carrinho, mas na vdd vamos usar o numeros vendidos
        return self.numero_de_vendidos

    @property   # por enquanto vai ser numeros no_carrinho, mas na vdd vamos usar o numeros vendidos
    def getNumerosDoCarrinho(self):
        return self.numeros_no_carrinho

    @property
    def getNumeroDeRestantes(self):
        return self.numero_de_restantes

    @property
    def getPorcentagemDeVendas(self):
        # ja em porcentagem  --> /1000 e  *100
        return self.numero_de_vendidos/10

    @property
    def getValorArrecadado(self):
        return self.valor_arrecadado

    @property
    def getListaNumRestantes(self):
        return self.lista_numeros_restantes
