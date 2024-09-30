from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', views.usuario, name='usuario'),
    # path('productos/', views.productos, name='productos'),
    path('productos/electronica/', views.electronica, name='electronica'),
    path('productos/juguetes/', views.juguetes, name='juguetes'),
    path('productos/ropa/', views.ropa, name='ropa'),
    path('productos/', views.productos, name='productos'),

    path('productos/juguetes/auto/', views.detalle_auto, name='detalle_auto'),
    path('productos/juguetes/muneca/', views.detalle_muneca, name='detalle_muneca'),
    path('productos/juguetes/bloques/', views.detalle_bloques, name='detalle_bloques'),
    path('productos/electronica/telefono/', views.detalle_telefono, name='detalle_telefono'),
    path('productos/electronica/portatil/', views.detalle_portatil, name='detalle_portatil'),
    path('productos/electronica/tablet/', views.detalle_tablet, name='detalle_tablet'),
    path('productos/ropa/', views.ropa, name='ropa'),
    path('productos/ropa/chaqueta/', views.detalle_chaqueta, name='detalle_chaqueta'),
    path('productos/ropa/camiseta/', views.detalle_camiseta, name='detalle_camiseta'),
    path('productos/ropa/jeans/', views.detalle_jeans, name='detalle_jeans'),
]

