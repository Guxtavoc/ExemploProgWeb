from django.shortcuts import get_object_or_404, render
from categoria.models import Categoria
from produtos.models import Produto

# Create your views here.
def visualizarLoja(request, categoria_slug = None):
    if categoria_slug!=None:
        cat = get_object_or_404(Categoria, slug = categoria_slug)
        produtos = Produto.objects.all().filter(categoria = cat, esta_disponivel = True)
    else :
        produtos = Produto.objects.all().filter(esta_disponivel = True)
    contexto = {
        'produtos' : produtos,
    }
    return render (request,'index.html',contexto)

def exibirDetalhesProduto(request, categoria_slug, produto_slug):
    produto = Produto.objects.get(categoria__slug = categoria_slug, slug = produto_slug)
    contexto = {
        'produto' : produto
    }
    return render(request, 'Loja/detalhes.html',contexto)