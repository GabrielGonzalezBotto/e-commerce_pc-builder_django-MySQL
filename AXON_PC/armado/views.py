from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from tienda.models import Producto

def asistente_armado(request):
    if 'carrito_armado' not in request.session:
        request.session['carrito_armado'] = {
            'procesador': None,
            'placa_madre': None,
            'memoria_ram': None,
            'tarjeta_grafica': None,
            'fuente': None,
            'gabinete': None,
            'almacenamiento': None,
            'pantalla': None,
            'accesorios': None,
        }
    armado = request.session['carrito_armado']

    #Paso 1
    paso_actual = 'procesador'
    productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='procesador', stock__gt=0)

    #paso 2
    if armado['procesador']:
        paso_actual = 'placa_madre'
        cpu_elegido = Producto.objects.filter(id=armado['procesador']).first() if armado['procesador'] != 'omitido' else None

        if cpu_elegido and cpu_elegido.socket:
            productos_filtrados = Producto.objects.filter(
                categoria__nombre__iexact='placa madre',
                socket__iexact=cpu_elegido.socket,
                stock__gt=0
            )
        else:
            productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='placa madre', stock__gt=0)

    #paso 3 
    if armado['procesador'] and armado['placa_madre']:
        paso_actual = 'memoria_ram'
        mother_elegida = Producto.objects.filter(id=armado['placa_madre']).first() if armado['placa_madre'] != 'omitido' else None

        if mother_elegida and mother_elegida.tipo_memoria:
            productos_filtrados = Producto.objects.filter(
                categoria__nombre__iexact='memoria ram',
                tipo_memoria__iexact=mother_elegida.tipo_memoria,
                stock__gt=0
            )
        else:
            productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='memoria ram', stock__gt=0)

    #paso 4
    if armado['procesador'] and armado['placa_madre'] and armado['memoria_ram']:
        paso_actual = 'tarjeta_grafica'
        productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='tarjeta grafica', stock__gt=0)


    #Pagincaion reutilizada de tienda.html
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
        'paso_titulo':titulos.get(paso_actual, paso_actual),
        'productos': page_obj,
        'armado':armado,
        'cpu_elegido': Producto.objects.filter(id=armado['procesador']).first() if armado['procesador'] != 'omitido' else None,
        'mother_elegida': Producto.objects.filter(id=armado['placa_madre']).first() if armado['placa_madre'] != 'omitido' else None,
        'ram_elegida': Producto.objects.filter(id=armado['memoria_ram']).first() if armado['memoria_ram'] != 'omitido' else None,
        'gpu_elegida': Producto.objects.filter(id=armado['tarjeta_grafica']).first() if armado['tarjeta_grafica'] != 'omitido' else None,
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

def omitir_paso(request, paso):
    armado = request.session.get('carrito_armado', {})
    if paso in armado:
        armado[paso] = 'omitido'
        request.session['carrito_armado'] = armado
        request.session.modified = True

    return redirect('asistente_armado')

def reiniciar_armado(request):
    if 'carrito_armado' in request.session:
        del request.session['carrito_aramdo']
    return redirect('asistente_armado')