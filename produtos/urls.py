from django.urls import path
from produtos import views


urlpatterns = [
    path('',views.visualizarProdutos, name='produto')
]