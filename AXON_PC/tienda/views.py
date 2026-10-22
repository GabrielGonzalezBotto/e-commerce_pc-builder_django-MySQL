from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Review
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

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

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        comentario = request.POST.get('comentario')
        stars = request.POST.get('stars', 5)

        Review.objects.create(
            producto=producto,
            ususario=request.user,
            comentario=comentario,
            stars=int(stars)
        )
        return redirect('producto', pk=producto.pk)
    
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

@login_required
def eliminar_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    producto_id = review.producto.id

    if review.ususario == request.user:
        review.delete()

    return redirect('producto', pk=producto_id)

@login_required
def editar_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    producto_id = review.producto.id

    if request.method == 'POST' and review.ususario == request.user:
        comentario_nuevo = request.POST.get('comentario')
        stars_nuevas = request.POST.get('stars')

        review.comentario = comentario_nuevo
        if stars_nuevas:
            review.stars = int(stars_nuevas)
        review.save()

    return redirect('producto', pk=producto_id)
