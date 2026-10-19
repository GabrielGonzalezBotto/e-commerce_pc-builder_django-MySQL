from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def tienda(request):
    productos = Producto.objects.all().order_by('id')
    paginator = Paginator(productos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'productos': page_obj,
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

@login_required
def toggle_favorito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    usuario = request.user

    if producto in usuario.favoritos.all():
        usuario.favoritos.remove(producto)
    else:
        usuario.favoritos.add(producto)

    if request.headers.get('x-request-with') == 'XMLHttpRequest':
        return JsonResponse({'status':'ok'})

    return redirect('tienda')
