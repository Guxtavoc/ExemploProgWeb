from django.shortcuts import get_object_or_404, redirect, render
from carrinho.models import Carrinho, carItem
from produtos.models import Produto
from django.core.exceptions import ObjectDoesNotExist

def _getCarId(request):
    car = request.session.session_key
    if not car:
        car = request.session.create()
    return car

def adicionarItemCarrinho(request,produto_id):
    produto = Produto.objects.get(id = produto_id)
    try:
        car = Carrinho.objects.get(car_id = _getCarId(request))
    except Carrinho.DoesNotExist:
        car = Carrinho.objects.create(car_id = _getCarId(request))
    car.save()

    try:
        car_item = carItem.objects.get(produto = produto,car = car)
        car_item.quantidade += 1
        car_item.save()
    except carItem.DoesNotExist:
        car_item= carItem.objects.create(
            produto = produto,
            quantidade = 1,
            car = car,
        )
    return redirect('carrinho')

def exibirCarrinho (request,total = 0, quantidade = 0, car_itens = None):
    try:
        car = Carrinho.objects.get(car_id = _getCarId(request))
        car_itens = carItem.objects.filter(car=car)
        for car_item in car_itens:
            total += (car_item.produto.preco * car_item.quantidade)
            quantidade += car_item.quantidade
    except ObjectDoesNotExist:
        pass
    contexto = {
        'total' : total,
        'quantidade' : quantidade,
        'car_itens' : car_itens,
    }
    
    return render(request,'loja/carrinho.html', contexto)

def diminuirQuantidadeProdutoCar(request, produto_id):
    car = Carrinho.objects.get(car_id=_getCarId(request))
    produto = get_object_or_404(Produto, id = produto_id)
    car_item = carItem.objects.get(produto = produto, car = car)
    if car_item.quantidade > 1:
        car_item.quantidade -= 1
        car_item.save()
    else:
        car_item.delete()
    return redirect('carrinho')

def removerItemCar(request, produto_id):
    car = Carrinho.objects.get(car_id=_getCarId(request))
    produto = get_object_or_404(Produto, id = produto_id)
    car_item = carItem.objects.get(produto = produto, car = car)
    car_item.delete()
    return redirect('carrinho')