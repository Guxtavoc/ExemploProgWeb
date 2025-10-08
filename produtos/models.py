from django.db import models
from django.urls import reverse
from categoria.models import Categoria

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField(max_length=300,blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    imagem = models.ImageField(upload_to='fotos/produtos',blank=True)
    estoque = models.IntegerField()
    esta_disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now=True)
    data_alteracao = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('detalhes_do_produto',args=[self.categoria.slug,self.slug])
