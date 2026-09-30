from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje

def productos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", 0) or 0
        cantidad = request.POST.get("cantidad", 0) or request.POST.get("Cantidad", 0) or 0
        mensaje = request.POST.get("mensaje", "").strip()

        if nombre:
            Mensaje.objects.create(
                nombre=nombre,
                categoria=categoria,
                precio=precio,
                cantidad=cantidad,
                mensaje=mensaje
            )
        return redirect('productos')
    
    mensajes = Mensaje.objects.all().order_by('-id')
    return render(request, "producto.html", {"mensajes": mensajes, "producto": None})

def editar(request, id):
    producto_obj = get_object_or_404(Mensaje, pk=id)
    if request.method == "POST":
        producto_obj.nombre = request.POST.get("nombre", "").strip()
        producto_obj.categoria = request.POST.get("categoria", "").strip()
        producto_obj.precio = request.POST.get("precio", 0) or 0
        producto_obj.cantidad = request.POST.get("cantidad", 0) or request.POST.get("Cantidad", 0) or 0
        producto_obj.mensaje = request.POST.get("mensaje", "").strip()
        producto_obj.save()
        return redirect('productos')
    
    mensajes = Mensaje.objects.all().order_by('-id')
    return render(request, "producto.html", {"mensajes": mensajes, "producto": producto_obj})

def eliminar(request, id):
    producto_obj = get_object_or_404(Mensaje, pk=id)
    producto_obj.delete()
    return redirect('productos')