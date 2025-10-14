from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Producto

# Personaliza el admin de usuarios
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)  # Desregistra el admin por defecto
admin.site.register(User, CustomUserAdmin)  # Registra el admin personalizado
admin.site.register(Producto) # Registra el modelo Producto
# admin.site.register(Group)  # Registra el modelo Group para gestionar grupos
