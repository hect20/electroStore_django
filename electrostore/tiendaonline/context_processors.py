from tiendaonline.models import Categoria

def all_categorias(request):
    return {'categorias':Categoria.objects.all(),}  # Can change numbers for more/fewer posts