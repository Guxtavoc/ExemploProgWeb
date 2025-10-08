from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    car_id = models.CharField(max_length= 40,blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.car_id

class carItem(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    car = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__ (self):
        return self.produto
    def subtotal(self):
        return self.produto.preco * self.quantidade