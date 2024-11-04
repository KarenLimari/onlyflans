from django.shortcuts import render

def index(request):
    # Lista de productos (puedes reemplazar esto con datos de una base de datos)
    productos = ["Producto 1", "Producto 2", "Producto 3"]
    return render(request, 'index.html', {'productos': productos})

def acerca(request):
    # Descripción del sitio y la PYME
    descripcion = "Este sitio web permite a los usuarios comprar productos de nuestra PYME."
    fecha_creacion = "Fecha de creación: 2024"
    return render(request, 'about.html', {'descripcion': descripcion, 'fecha_creacion': fecha_creacion})

def bienvenido(request):
    # Mensaje de bienvenida
    usuario = "Juan Perez"  # Cambia esto según la lógica de tu aplicación
    return render(request, 'welcome.html', {'usuario': usuario})
