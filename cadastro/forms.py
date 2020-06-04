from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Anuncio, Categoria
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class FormUserCadastro(UserCreationForm):
    data_nascimento = forms.DateField(widget=(DateInput()))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "data_nascimento",
            "password1",
            "password2",
        ]


class FormEditProfile(UserChangeForm):
    data_nascimento = forms.DateField(widget=(DateInput()))

    class Meta:

        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "data_nascimento",
            "password",
        ]


class FormChangePassword(PasswordChangeForm):

    class Meta:
        model = User

# eiqNUFyq6MZRe76


class CadastraAnuncio(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = [
            'text_color', 'titulo_anuncio', 'ano_fabricacao', 'descricao_breve', 'descricao_completa',
            'preco', 'imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5'
        ]

    def clean_ano_fabricacao(self):
        ano_fabricacao = self.cleaned_data.get("ano_fabricacao")
        if ano_fabricacao < 1920:
            raise forms.ValidationError(
                'O ano de fabricação deve conter 4 digitos, e ser posterior a 1920'
            )
        if timezone.now().year < ano_fabricacao:
            raise forms.ValidationError(
                'Ano inválido, ainda estamos em ' +
                str(timezone.now().year) + '!'
            )
        return ano_fabricacao


class FormCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'nome', 'nome_apresentavel',
        ]
