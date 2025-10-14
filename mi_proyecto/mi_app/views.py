from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Group, User
from .models import Producto
from .forms import ProductoForm

def inicio(request):
    if request.user.is_authenticated:
        return redirect('lista_productos')  # Redirige a lista_productos si el usuario está autenticado
    return render(request, 'mi_app/inicio.html')  # Muestra la página de inicio si no está autenticado

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar al grupo "Usuarios Regulares"
            grupo_regular, _ = Group.objects.get_or_create(name='Usuarios Regulares')
            user.groups.add(grupo_regular)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('lista_productos')
    else:
        form = UserCreationForm()
    return render(request, 'mi_app/registro.html', {'form': form})

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    es_administrador = request.user.groups.filter(name='Administradores').exists()
    return render(request, 'mi_app/lista_productos.html', {
        'productos': productos,
        'es_administrador': es_administrador
    })

@permission_required('mi_app.add_producto')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/agregar_producto.html', {'form': form})

def es_administrador(user):
    return user.groups.filter(name='Administradores').exists()

@user_passes_test(es_administrador)
def admin_view(request):
    return render(request, 'mi_app/admin_view.html')

@user_passes_test(es_administrador)
def gestionar_usuarios(request):
    usuarios = User.objects.all().prefetch_related('groups')
    return render(request, 'mi_app/gestionar_usuarios.html', {'usuarios': usuarios})

@user_passes_test(es_administrador)
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    grupos = Group.objects.all()

    if request.method == 'POST':
        # Actualizar datos básicos
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.is_staff = 'is_staff' in request.POST

        # Actualizar grupos
        grupo_ids = request.POST.getlist('groups')
        usuario.groups.set(grupo_ids)

        usuario.save()
        return redirect('gestionar_usuarios')

    return render(request, 'mi_app/editar_usuario.html', {
        'usuario': usuario,
        'grupos': grupos
    })