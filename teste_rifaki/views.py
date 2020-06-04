from django.shortcuts import render, get_object_or_404
from cadastro.views import Anuncio
from teste_rifaki.myClasses import Categoria, Expositor, ControladorCategorias, ControladorExpositor, Pesquisador
from compras.models import NumeroDaSorte, Carrinho


from django.utils import timezone

# adicionar os dois metodos a baixo ao contrutor para ja ser executado na criacao
controlador_expositores = ControladorExpositor()
pesquisador = Pesquisador()


def index(request):
    # sem parametro preenche o expositor index
    controlador_expositores.preencheExpositores()

    # inutilzada pq ainda não sei como atualizar os anuncios que foram modificados
    # controlador_expositores.atualizaExpositoresIndex()
    # controlador_expositores.preencheExpositores()          criar metodo atualizar que não renderiza tudo de novo

    context = {'controlador_expositores': controlador_expositores}

    if request.user.is_authenticated:
        users_carrinho = Carrinho.objects.get(proprietario=request.user)
        itens = users_carrinho.itens.all()
        context['users_carrinho'] = users_carrinho
        context['itens_no_carrinho'] = itens

    query = ''
    resultados = None
    if request.GET:
        # print(request.GET)
        query = request.GET['q']
        context['query'] = str(query)
        resultados = pesquisador.pesquisaPraMim(query)
        expositores_pesquisa = controlador_expositores.preencheExpositores(
            data=resultados)

        context['resultados'] = resultados
        print(resultados)

    return render(request, 'teste_rifaki/html/index.html', context)


def detail_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)

    usuario = request.user
    context = {'anuncio': anuncio, 'usuario': usuario}

    if usuario.is_authenticated:
        users_carrinho = Carrinho.objects.get(proprietario=usuario)
        itens = users_carrinho.itens.all()
        context['users_carrinho'] = users_carrinho
        context['itens_no_carrinho'] = itens

        if request.method == "POST":
            list_numeros_selecionados = request.POST['num_selected'].split(',')
            # enviar uma caixa de alerta de sucesso para o comprador "Seus números foram colocados no carrinho" -------------------- To Do
            print('lista de numeros enviados para o carrinho: ' +
                  str(list_numeros_selecionados))

            for numero in list_numeros_selecionados:
                numero_da_sorte = NumeroDaSorte()
                numero_da_sorte.numero_escolhido = int(numero)
                numero_da_sorte.anuncio_escolhido = anuncio
                numero_da_sorte.comprador = usuario
                numero_da_sorte.save()
                users_carrinho.itens.add(numero_da_sorte)
                users_carrinho.data_ultima_modificacao = timezone.now()
                users_carrinho.save()

    return render(request, 'teste_rifaki/html/detail.html', context)


def view_profile_anuncios(request):
    context = {'controlador_expositores': controlador_expositores}

    if request.user.is_authenticated:
        users_carrinho = Carrinho.objects.get(proprietario=request.user)
        itens = users_carrinho.itens.all()
        context['users_carrinho'] = users_carrinho
        context['itens_no_carrinho'] = itens

    if request.user.is_authenticated:
        expositores = controlador_expositores.preencheExpositores(
            data=request.user)
        context['expositores'] = expositores
        return render(request, 'teste_rifaki/html/view_anuncios.html', context)
    else:
        return redirect('/login')
