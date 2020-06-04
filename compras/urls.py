from django.urls import path

from . import views

app_name = 'compras'
urlpatterns = [
    path('carrinho/', views.view_carrinho, name='view_carrinho'),
    path('carrinho/<int:id_NumeroDaSorte>/delete',
         views.delete_do_carrinho, name='delete_do_carrinho'),
    path('<int:anuncio_id>/analisar/',
         views.view_pagina_vendas, name='view_pagina_vendas'),
]
