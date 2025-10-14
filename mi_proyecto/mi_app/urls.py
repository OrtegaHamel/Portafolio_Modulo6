from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('gestionar_usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('editar-usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
]

