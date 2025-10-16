
from carrinho.models import Carrinho, carItem
from carrinho.views import _getCarId


def contador(request):
    car_cont = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Carrinho.objects.filter(car_id=_getCarId(request))
            car_items = carItem.objects.all().filter(car = cart[:1])
            for car_item in car_items:
                car_cont += car_item.quantidade
        except Carrinho.DoesNotExist:
            car_cont = 0
    return dict(contador=car_cont)