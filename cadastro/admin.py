from django.contrib import admin

from .models import Anuncio


class AnuncioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['titulo_anuncio']}),
        (None,          {'fields': ['descricao_breve']}),
        (None,          {'fields': ['descricao_completa']}),
        (None,          {'fields': ['imagem1']}),
        (None,          {'fields': ['imagem2']}),
        (None,          {'fields': ['imagem3']}),
        (None,          {'fields': ['imagem4']}),
        (None,          {'fields': ['imagem5']}),
        (None,          {'fields': ['anunciante']}),
    ]


admin.site.register(Anuncio, AnuncioAdmin)
