from django.urls import path
from . import views 
from django.urls import include

urlpatterns = [
    path('', views.inicio),
    path('tienda', views.tienda),
    path('mapa',views.mapa),
    path('clima',views.clima),
    path('agregarCarrito/<id>',views.agregarCarrito),
    path('eliminarCarrito/<id>',views.eliminarCarrito),
    path('aumentar/<id>',views.aumentar),
    path('disminuir/<id>',views.disminuir),
]