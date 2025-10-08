from django.urls import path
from loja import views


urlpatterns = [
    path('',views.visualizarLoja, name = 'Loja'),
    path('<slug:categoria_slug>/', views.visualizarLoja, name = 'produtos_por_categoria'),
    path('<slug:categoria_slug>/<slug:produto_slug>/', views.exibirDetalhesProduto, name='detalhes_do_produto'),
]