from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_app/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/agregar_producto.html', {'form': form})