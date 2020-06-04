from django.urls import path

from . import views

app_name = 'cadastro'
urlpatterns = [
    path('user/', views.create_user, name='create_user'),
    path('anuncio/', views.cadastro_anuncio, name='cadastro_anuncio'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('<int:anuncio_id>/edit/',
         views.edit_anuncio, name='edit_anuncio'),
    path('profile/password/', views.edit_password, name='edit_password'),
    path('categorias/', views.cria_categoria, name='cria_categoria'),
    path('categorias/list/', views.view_categorias, name='view_categorias'),
    path('categorias/list/<int:categoria_id>/delete/',
         views.delete_categoria, name='delete_categoria'),
    path('categorias/list/<int:categoria_id>/edit/',
         views.edit_categoria, name='edit_categoria'),
]
