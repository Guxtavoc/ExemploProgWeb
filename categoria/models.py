from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length= 100, unique= True)
    descricao = models.TextField(max_length= 255, blank= True)
    categoria_imagem = models.ImageField(upload_to='fotos/categorias/',blank=True)

    def __str__(self):
        return self.categoria_name
    
    def get_url(self):
        return reverse('produtos_por_categoria', args=[self.slug])