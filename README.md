# Portafolio Modulo 6 - Aplicación Web con Django
Por Álvaro Ortega Hamel

**Repositorio:** [Portafolio_Modulo6](https://github.com/OrtegaHamel/Portafolio_Modulo6.git)

---
## **Descripción del Proyecto**
Este proyecto es una aplicación web desarrollada con **Django**, diseñada para gestionar productos y usuarios. Incluye funcionalidades como autenticación, autorización, gestión de productos, y un panel de administración personalizado para gestionar usuarios y permisos.

---
## **Características Principales**
- **Autenticación y Autorización:** Registro, inicio de sesión, y cierre de sesión de usuarios.
- **Gestión de Productos:** Listar, agregar y editar productos.
- **Gestión de Usuarios:** Panel de administración para gestionar usuarios, grupos y permisos.
- **Roles de Usuario:** Usuarios regulares y administradores, con permisos diferenciados.
- **Interfaz Dinámica:** Uso de templates para mostrar contenido dinámico.

---
## **Estructura del Proyecto**

```
mi_proyecto/
│
├── mi_app/
│   ├── migrations/
│   ├── templates/
│   │   └── mi_app/
│   │       ├── base.html
│   │       ├── inicio.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── registro.html
│   │       ├── lista_productos.html
│   │       ├── agregar_producto.html
│   │       ├── gestionar_usuarios.html
│   │       └── editar_usuario.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── mi_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── caracteristicas.md
└── README.md
```



---
## **Requerimientos Funcionales Cumplidos**

### **1. Características de Django para Aplicaciones Empresariales**
- **Desarrollo Rápido:** Django permite crear aplicaciones web de manera rápida gracias a su estructura predefinida y herramientas integradas.
- **Escalabilidad:** Facilita el crecimiento de la aplicación con su arquitectura modular.
- **Seguridad:** Incluye protección contra ataques comunes como CSRF, XSS, y SQL Injection.
- **Administración Integrada:** Proporciona un panel de administración automático para gestionar modelos.

### **2. Configuración del Proyecto**
- **Creación del Proyecto:** Usando `django-admin startproject mi_proyecto`.
- **Creación de la Aplicación:** Usando `python manage.py startapp mi_app`.

### **3. Templates para Contenido Dinámico**
- **Uso de Templates:** Los templates permiten mostrar contenido dinámico proveniente de la base de datos.
- **Ejemplo:** La página `lista_productos.html` muestra una lista de productos almacenados en la base de datos.

### **4. Formularios para Captura de Información**
- **Formularios de Django:** Se utilizan para registrar usuarios, agregar productos, y editar información.
- **Ejemplo:** El formulario en `registro.html` permite registrar nuevos usuarios.

### **5. Autenticación y Autorización**
- **Sistema de Autenticación:** Django proporciona vistas y formularios preconstruidos para el inicio de sesión, registro y cierre de sesión.
- **Control de Accesos:** Se implementan decoradores como `@login_required` y `@user_passes_test` para restringir el acceso a ciertas vistas según el rol del usuario.

### **6. Módulo de Administración de Usuarios y Permisos**
- **Panel de Administración:** Se personaliza el panel de administración de Django para gestionar usuarios, grupos y permisos.
- **Vista de Gestión de Usuarios:** La vista `gestionar_usuarios` permite a los administradores gestionar los permisos y roles de los usuarios.

---
## **Funcionamiento de la Aplicación**

### **1. Registro de Usuarios**
- **Por Defecto:** Al registrar un nuevo usuario, este queda como **usuario regular**, con permisos mínimos.
- **Proceso:** Los usuarios se registran a través del formulario en `registro.html`.

### **2. Inicio de Sesión**
- **Validación:** El formulario de inicio de sesión valida las credenciales y muestra una alerta si son incorrectas.
- **Redirección:** Los usuarios autenticados son redirigidos a la lista de productos.

### **3. Gestión de Productos**
- **Listar Productos:** La vista `lista_productos` muestra todos los productos disponibles.
- **Agregar Productos:** La vista `agregar_producto` permite a los usuarios agregar nuevos productos.

### **4. Gestión de Usuarios**
- **Panel de Administración:** Los administradores pueden gestionar usuarios, grupos y permisos desde la vista `gestionar_usuarios`.
- **Editar Usuarios:** La vista `editar_usuario` permite modificar los datos de un usuario específico.

---
## **Credenciales de Administrador**
- **Usuario:** `administrador`
- **Contraseña:** `contrasena123`
Con este usuario, se pueden administrar los permisos de los demás usuarios e incluso nombrarlos administradores.

---
## **Instalación y Ejecución**

### **Clonar el Repositorio**
```bash
git clone git@github.com\:OrtegaHamel/Portafolio_Modulo6.git
cd Portafolio_Modulo6
```

### **Configurar el Entorno Virtual**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **Configurar la Base de Datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Crear un Superusuario (Opcional)**
```bash
 python manage.py createsuperuser
```
### **Ejecutar el Servidor
```bash
python manage.py runserver
```

## **Tecnologías Utilizadas**
```bash
Backend: Django 5.2.7
Frontend: HTML, CSS, Bootstrap 5.3
Base de Datos: SQLite (por defecto)
```