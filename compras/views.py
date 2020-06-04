from .models import Carrinho, NumeroDaSorte
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .myClasses import ControladorDeCompras
from cadastro.models import Anuncio
from .forms import FormRegisterVenda
from django.contrib.auth.models import User


controlador_vendas = ControladorDeCompras()

# ------------- CARRINHO PAGE'S VIEWS --------------- #


def view_carrinho(request):
    context = {}
    if request.user.is_authenticated:
        try:
            users_carrinho = Carrinho.objects.get(proprietario=request.user)
            itens = users_carrinho.itens.all()
            context['users_carrinho'] = users_carrinho
            context['itens_no_carrinho'] = itens
        except:
            carrinho = Carrinho()
            carrinho.proprietario = request.user
            carrinho.data_ultima_modificacao = timezone.now()
            carrinho.save()

            itens = users_carrinho.itens.all()
            context['users_carrinho'] = users_carrinho
            context['itens_no_carrinho'] = itens

            print('Criamos um carrinho pra ti!')

        return render(request, 'compras/view_pages/view_carrinho.html', context)
    else:
        return redirect('/login')


def delete_do_carrinho(request, id_NumeroDaSorte):
    numero_excluido = get_object_or_404(NumeroDaSorte, pk=id_NumeroDaSorte)
    if numero_excluido.comprador == request.user:
        numero_excluido.delete()

        return HttpResponseRedirect(reverse('compras:view_carrinho'))
    else:
        redirect('compras:view_carrinho')


# ------------- ANALISE PAGE'S VIEWS --------------- #
def view_pagina_vendas(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    numeros_da_sorte = NumeroDaSorte.objects.filter(anuncio_escolhido=anuncio)

    if anuncio.anunciante == request.user:
        controlador_vendas.getTheNumbersOfAnuncio(anuncio)

        if request.method == "POST":
            form = FormRegisterVenda(
                request.POST, controlador_vendas=controlador_vendas)

            if form.is_valid():

                venda = form.save(commit=False)

                comprador = get_object_or_404(
                    User, username=request.POST['username'])
                venda.comprador_user = comprador

                venda.vendedor_user = request.user

                venda.data_de_registro = request.POST['data_de_registro']

                for number in numeros_da_sorte:
                    if number.numero_escolhido == int(request.POST['numero_vendido_form']):
                        venda.numero_vendido = number

                venda.valor = anuncio.preco

                # venda.save()

                form = FormRegisterVenda(
                    controlador_vendas=controlador_vendas)
                context = {
                    'form': form,
                    'anuncio': anuncio,
                    'controlador_vendas': controlador_vendas,
                }

                return render(request, 'compras/view_pages/view_pagina_vendas.html', context)
        else:
            form = FormRegisterVenda(controlador_vendas=controlador_vendas)

        context = {
            'form': form,
            'anuncio': anuncio,
            'controlador_vendas': controlador_vendas,
        }
        return render(request, 'compras/view_pages/view_pagina_vendas.html', context)
    else:
        return redirect('/')
