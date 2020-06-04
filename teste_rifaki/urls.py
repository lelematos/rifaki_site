from django.urls import path

from . import views

app_name = 'teste_rifaki'
urlpatterns = [
    # ex: /teste_rifaki/
    path('', views.index, name='index'),
    # ex: /teste_rifaki/<algum id>
    path('<int:anuncio_id>/', views.detail_anuncio, name='detail'),
    #     # ex: /teste_rifaki/cadastro_anuncio
    path('anuncios/', views.view_profile_anuncios,
         name='view_profile_anuncios'),
]


"""     # ex: /firstapp/algum_id
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /firstapp/algum_id/result
    path('<int:question_id>/result/', views.results, name='result'),
    # ex: /firstapp/algum_id/vote
    path('<int:question_id>/vote/', views.vote, name='vote'), """
