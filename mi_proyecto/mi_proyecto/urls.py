from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from mi_app import views

def redirect_to_inicio(request):
    return redirect('inicio')

urlpatterns = [
    path('admin/', redirect_to_inicio),  # Redirige a inicio en lugar de mostrar el admin de Django
    path('secret-admin/', admin.site.urls),  # Cambia la URL del admin a algo menos obvio
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='mi_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('productos/', include('mi_app.urls')),
]

