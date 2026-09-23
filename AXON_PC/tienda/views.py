from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def tienda(request):
    #render toma el request y el HTML para mostrar
    return render(request, 'tienda/tienda.html')

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
