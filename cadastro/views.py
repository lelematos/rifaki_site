from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import FormUserCadastro, CadastraAnuncio, FormEditProfile, FormChangePassword, FormCategoria
from .models import Anuncio, Categoria
from django.contrib.auth import authenticate, login, update_session_auth_hash
from teste_rifaki.myClasses import ControladorCategorias, ControladorExpositor
from django.db.models import Q
from compras.models import Carrinho, NumeroDaSorte

from django.utils import timezone

from django.contrib.auth.forms import PasswordChangeForm


id_atual = 0

controlador_categorias = ControladorCategorias()


# ------------- USER'S VIEWS --------------- #
def create_user(request):
    form = FormUserCadastro(request.POST)
    if request.method == "POST":
        if form.is_valid():
            request.user = form.save(commit=False)
            request.user.m_data_nascimento = request.POST['data_nascimento']
            request.user.save()

            carrinho = Carrinho()
            carrinho.proprietario = request.user
            carrinho.data_ultima_modificacao = timezone.now()
            carrinho.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
    else:
        form = FormUserCadastro()

    return render(request, "cadastro/creation_pages/create_user.html", {'form': form})


def view_profile(request):
    if request.user.is_authenticated:
        args = {'usuario': request.user}
        return render(request, "cadastro/view_pages/view_profile.html", args)
    else:
        return redirect('/login')


def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = FormEditProfile(request.POST, instance=user)
        if request.method == "POST":
            if form.is_valid():
                user = form.save(commit=False)
                print((request.POST['data_nascimento']))
                user.m_data_nascimento = request.POST['data_nascimento']
                user.save()

                return redirect('/cadastro/profile')
            # aplicaInfosAoUser(request.user, form)
        else:
            form = FormEditProfile(instance=request.user)

            form.data_nascimento = request.user.m_data_nascimento
            print(form.data_nascimento)

        return render(request, "cadastro/edit_pages/edit_user.html", {'form': form, 'usuario': user})
    else:
        return redirect('/login')


def edit_password(request):
    if request.user.is_authenticated:
        usuario = request.user
        form = PasswordChangeForm(data=request.POST, user=usuario)
        if request.method == "POST":
            if form.is_valid():
                print('salvado')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/cadastro/profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'cadastro/edit_pages/edit_password.html', {'form': form})
    else:
        return redirect('/login')


# ------------- ANUNCIOS' VIEWS --------------- #
def cadastro_anuncio(request):
    if request.user.is_authenticated:
        global id_atual
        usuario = request.user
        if request.method == "POST" and usuario.is_authenticated:
            form = CadastraAnuncio(request.POST, request.FILES)
            if form.is_valid():
                anuncio = form.save(commit=False)
                anuncio.anunciante = usuario
                anuncio.data_publi = timezone.now()
                controlador_categorias.verificaCategoriasDesteAnuncio(anuncio)
                anuncio.mem_categorias = anuncio.categoria
                anuncio.identificador_anuncio = id_atual+1
                anuncio.save()
                id_atual += 1
                return HttpResponseRedirect(reverse('teste_rifaki:detail', args=(anuncio.id,)))
        else:
            form = CadastraAnuncio()

        return render(request, 'cadastro/creation_pages/create_anuncio.html', {'form': form, 'usuario': usuario})
    else:
        return redirect('/login')


def edit_anuncio(request, anuncio_id):
    if request.user.is_authenticated:
        usuario = request.user
        anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
        # anuncio = Anuncio.objects.get(id=anuncio_id)
        if request.method == "POST":
            form = CadastraAnuncio(
                request.POST, request.FILES, instance=anuncio)
            if form.is_valid():
                anuncio = form.save(commit=False)
                controlador_categorias.verificaCategoriasDesteAnuncio(anuncio)
                anuncio.mem_categorias = anuncio.categoria
                anuncio.save()
                return HttpResponseRedirect(reverse('teste_rifaki:view_profile_anuncios'))
        else:
            form = CadastraAnuncio(instance=anuncio)

        return render(request, 'cadastro/edit_pages/edit_anuncio.html', {'form': form, 'anuncio': anuncio})
    else:
        return redirect('/login')


# ------------- CATEGORIAS' VIEWS --------------- #
def cria_categoria(request):
    if request.user.is_superuser:
        btn_text = 'criar categoria'
        if request.method == 'POST':
            form = FormCategoria(request.POST)
            if form.is_valid():
                categoria = form.save(commit=False)
                categoria.criador = request.user
                categoria.data_de_criacao = timezone.now()
                categoria.save()

                return HttpResponseRedirect(reverse('cadastro:view_categorias'))
        else:
            form = FormCategoria()
        return render(request, 'cadastro/creation_pages/create_categoria.html', {'form': form, 'btn_text': btn_text})

    else:
        return redirect('/')


def delete_categoria(request, categoria_id):
    if request.user.is_superuser:
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        categoria.delete()
        return HttpResponseRedirect(reverse('cadastro:view_categorias'))
    else:
        return redirect('/')


def edit_categoria(request, categoria_id):
    if request.user.is_superuser:
        btn_text = 'salvar'
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        if request.method == 'POST':
            form = FormCategoria(request.POST, instance=categoria)
            if form.is_valid():
                categoria = form.save(commit=False)
                categoria.criador = request.user    # criador ==> editor
                categoria.data_de_criacao = timezone.now()  # data de edição no caso
                categoria.save()

                return HttpResponseRedirect(reverse('cadastro:view_categorias'))
        else:
            form = FormCategoria(instance=categoria)
        return render(request, 'cadastro/creation_pages/create_categoria.html', {'form': form, 'btn_text': btn_text})

    else:
        return redirect('/')


def view_categorias(request):
    if request.user.is_superuser:
        lista_categorias_existentes = Categoria.objects.all()
        return render(request, 'cadastro/view_pages/view_categorias.html', {'lista_categorias_existentes': lista_categorias_existentes})
    else:
        return redirect('/')
