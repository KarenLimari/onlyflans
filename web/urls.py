from django.urls import path
from .views import index, acerca, bienvenido

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', acerca, name='acerca'),
    path('bienvenido/', bienvenido, name='bienvenido'),
]
