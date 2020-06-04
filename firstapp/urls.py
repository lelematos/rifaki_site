from django.urls import path

from . import views

app_name = 'firstapp'
urlpatterns = [
    # ex: /firstapp/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /firstapp/algum_id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /firstapp/algum_id/result
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /firstapp/algum_id/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]