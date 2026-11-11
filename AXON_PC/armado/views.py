from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto, Categoria
from django.core.paginator import Paginator

# Create your views here.
def asistente_armado(request):
    if 'carrito_armado' not in request.session:
        request.session['carrito_armado'] = {
            'procesador': None,
            'placa_madre': None,
            'memoria_ram': None,
            'tarjeta_grafica': None,
            'fuente': None,
            'gabinete': None,
            'almacenamineto': None,
        }
    armado = request.session['carrito_armado']
    paso_actual = 'procesador' #por default
    productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='procesador')

    if armado['procesador']:
        paso_actual = 'placa_madre'
        cpu_elegido = Producto.objects.get(id=armado['procesador'])

        productos_filtrados = Producto.objects.filter(
            categoria__nombre__iexact='placa_madre',
            socket=cpu_elegido.socket
        )

    if armado['procesador'] and armado['placa_madre']:
        paso_actual = 'memoria_ram'
        mother_elegida = Producto.objects.get(id=armado['placa_madre'])

        productos_filtrados = Producto.objects.filter(
            categoria__nombre__iexact='memoria ram',
            tipo_memoria=mother_elegida.tipo_memoria
        )

    if armado['procesador'] and armado['placa_madre'] and armado['memoria_ram']:
        paso_actual = 'tarjeta_grafica'
        productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='tarjeta grafica')

    #Reutiizo la paginacion de mi seccion de tienda
    paginator = Paginator(productos_filtrados, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    

    titulos = {
        'procesador': 'Procesador',
        'placa_madre': 'Placa Madre',
        'memoria_ram': 'Memoria RAM',
        'tarjeta_grafica': 'Tarjeta Gráfica'
    }

    context = {
        'paso_actual': paso_actual,
        'paso_titulo': titulos.get(paso_actual, paso_actual), # <-- NUEVA VARIABLE LIMPIA
        'productos': productos_filtrados,
        'cpu_elegido': Producto.objects.filter(id=armado['procesador']).first(),
        'mother_elegida': Producto.objects.filter(id=armado['placa_madre']).first(),
        'ram_elegida': Producto.objects.filter(id=armado['memoria_ram']).first(),
        'gpu_elegida': Producto.objects.filter(id=armado['tarjeta_grafica']).first(),
        'productos': page_obj,
    }
    
    return render(request, 'armado/asistente.html', context)

def seleccionar_componente(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categoria = producto.categoria.nombre.lower()

    armado = request.session.get('carrito_armado', {})

    if 'procesador' in categoria:
        armado['procesador'] = producto.id
    elif 'placa madre' in categoria:
        armado['placa_madre'] = producto.id
    elif 'memoria ram' in categoria:
        armado['memoria_ram'] = producto.id
    elif 'tarjeta grafica' in categoria:
        armado['tarjeta_grafica'] = producto.id

    request.session['carrito_armado'] = armado
    request.session.modified = True

    return redirect('asistente_armado')

def reiniciar_armado(request):
    if 'carrito_armado' in request.session:
        del request.session['carrito_armado']
    return redirect('asistente_armado')