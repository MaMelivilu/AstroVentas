from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .cart import Cart
from django.urls import reverse
import os 
from django.conf import settings
from django.http import JsonResponse

# Create your views here.

def inicio(request):
    ids_productos = [11,12,5,6]  # IDs de productos que quieres obtener
    productos_inicio = Productos.objects.filter(id__in=ids_productos)
    carrito = Carrito.objects.all()
   
    return render(request, "inicio.html",{"prod":productos_inicio,"car": carrito})

def mapa(request):
    carrito = Carrito.objects.all()
    return render(request, "mapa.html",{"car": carrito})

def clima(request):
    carrito = Carrito.objects.all()
    return render(request, "clima.html",{"car": carrito})

def tienda(request):
    productos = Productos.objects.all()
    carrito = Carrito.objects.all()


    return render(request, "tienda.html", {"prod": productos,"car": carrito})

def agregarCarrito(request, id):
    producto = get_object_or_404(Productos, id=id)
    carrito_existente = Carrito.objects.filter(nombre=producto.nombre).first()
    
    if carrito_existente:
        # Si el producto ya está en el carrito, incrementamos la cantidad
        carrito_existente.cantidad += 1
        carrito_existente.save()
    else:
        # Si el producto no está en el carrito, lo añadimos
        Carrito.objects.create(nombre=producto.nombre, precio=producto.precio, image=producto.image)
        
    return redirect('/tienda')

def eliminarCarrito(request,id):
    print("ELIMINAR CARRITO",id)
    carrito = Carrito.objects.get(id = id)
    carrito.delete()
    return redirect('/tienda')

def aumentar(request,id):
    carro = get_object_or_404(Carrito, id = id)
    carro.cantidad += 1
    carro.save()
    return redirect('/tienda')

def disminuir(request,id):
    carro = get_object_or_404(Carrito, id = id)
    
    if carro.cantidad <= 1:
        carro.delete()
    else:
        carro.cantidad -= 1
        carro.save()
        
    return redirect('/tienda')


    

         

    