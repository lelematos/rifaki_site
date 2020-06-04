from django.shortcuts import get_object_or_404
from django import forms
from django.contrib.auth.models import User
from cadastro.models import Anuncio, Categoria
from .models import Venda, NumeroDaSorte, Carrinho


class DateInput(forms.DateInput):
    input_type = 'date'


class FormRegisterVenda(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.controlador = kwargs.pop('controlador_vendas')
        super(FormRegisterVenda, self).__init__(*args, **kwargs)

    username = forms.CharField(
        max_length=100, label="Username do comprador:")

    data_de_registro = forms.DateField(
        widget=(DateInput()), label="Data da venda:")

    numero_vendido_form = forms.IntegerField(label="Digite o número vendido:")

    class Meta:
        model = Venda
        fields = [
            'username',
            'numero_vendido_form',
            'data_de_registro',
        ]

    def clean_numero_vendido_form(self):
        numero_vendido_form = self.cleaned_data.get("numero_vendido_form")
        if len(str(numero_vendido_form)) != 3:
            raise forms.ValidationError(
                "Digite o número em um formato valido, com três digitos. Ex.: 005"
            )
        if numero_vendido_form not in self.controlador.getListaNumRestantes:
            raise forms.ValidationError(
                "Desculpe, este número já esta registrado como vendido em nosso sistema!"
            )
        return numero_vendido_form

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = get_object_or_404(User, username=username)
        except:
            raise forms.ValidationError(
                'Este usuario não esta cadastrado em nosso sistema!'
            )


# class FormRegisterVenda(forms.ModelForm):

#     """ def __init__(self, *args, **kwargs):
#         self.controlador = kwargs.pop('controlador_vendas')
#         super(FormRegisterVenda, self).__init__(*args, **kwargs) """

#     username = forms.CharField(
#         max_length=100, label="Username do comprador:")

#     data_de_registro = forms.DateField(
#         widget=(DateInput()), label="Data da venda:")

#     numero_vendido_form = forms.IntegerField(label="Digite o número vendido:")

#     class Meta:
#         model = Venda
#         fields = [
#             'username',
#             'numero_vendido_form',
#             'data_de_registro',
#         ]

#     def clean_numero_vendido_form(self, *args, **kwargs):
#         cleaned_data = self.clean()
#         numero = cleaned_data.get("numero_vendido_form")
#         print(numero)
#         # print(self.controlador.getListaNumRestantes)
#         if len(str(numero)) == 3:
#             return numero
#         else:
#             self.add_error('shortcodeurl', "The url is not valid")
#             # raise forms.ValidationError(
#             #     "Digite o número em um formato valido, com três digitos. Ex.: 005"
#             # )
#         # if numero not in self.controlador.getListaNumRestantes:
#         #     raise forms.ValidationError(
#         #         "Desculpe, este número já esta registrado como vendido em nosso sistema!"
#         #     )
