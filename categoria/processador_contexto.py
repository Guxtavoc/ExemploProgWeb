from categoria.models import Categoria


def listarCategorias(request):
    display = Categoria.objects.all()
    return dict(cats=display)