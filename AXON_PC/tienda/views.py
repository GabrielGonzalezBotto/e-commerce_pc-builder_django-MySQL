from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()

    context = {
        'productos': productos,
    }
    
    return render(request, 'tienda/tienda.html', context)

def producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    especificaciones = producto.especificaciones.all()
    review = producto.reviews.all()

    context = {
        'producto': producto,
        'especificaciones': especificaciones,
        'review': review,
    }

    return render(request, 'tienda/producto.html', context)
