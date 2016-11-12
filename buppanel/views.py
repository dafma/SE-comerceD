from django.shortcuts import render
from shop.models import Producto, Categoria

# Create your views here.

def panel(request):
	productos = Producto.objects.all()
	categorias = Categoria.objects.all()
	return render(request,'panel_principal.html', 
												{'productos': productos,
												  'categorias':categorias})