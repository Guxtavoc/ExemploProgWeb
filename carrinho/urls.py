from django.urls import path
from carrinho import views


urlpatterns = [
    path('',views.exibirCarrinho, name = 'carrinho'),
    path('adicionar_car/<int:produto_id>/',views.adicionarItemCarrinho, name = 'adicionar_car'),
    path('diminuir_item_car/<int:produto_id>', views.diminuirQuantidadeProdutoCar, name = 'diminuir_item_car'),
    path('remover_item_car/<int:produto_id>',views.removerItemCar, name = 'remover_item_car'),
]