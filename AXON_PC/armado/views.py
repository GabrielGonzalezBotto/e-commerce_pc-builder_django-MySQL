from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from tienda.models import Producto

ORDEN_PASOS = ['procesador', 'placa_madre', 'memoria_ram', 'tarjeta_grafica']

def asistente_armado(request):
    if 'carrito_armado' not in request.session:
        request.session['carrito_armado'] = {
            'procesador': None,
            'placa_madre':None,
            'memoria_ram': None,
            'tarjeta_grafica': None,
        }
    armado = request.session['carrito_armado']

    #poder retroceder un paso en la lista
    paso_forzado = request.GET.get('paso')
    armado_completo = False

    if paso_forzado in ORDEN_PASOS:
        paso_actual = paso_forzado
    else:
        paso_actual = None
        for paso in ORDEN_PASOS:
            if not armado.get(paso):
                paso_actual = paso
                break

        if not paso_actual:
            armado_completo = True
            paso_actual = 'finalizado'

    productos_filtrados = Producto.objects.none()

    if paso_actual == 'procesador':
        productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='procesador', stock__gt=0)
    elif paso_actual == 'placa_madre':
        cpu_id = armado.get('preocesador')
        cpu_elegido = Producto.objects.filter(id=cpu_id).first() if cpu_id and cpu_id != 'omitido' else None

        if cpu_elegido and cpu_elegido.socket:
            productos_filtrados = Producto.objects.filter(
                categoria__nombre__iexact='placa madre',
                socket__ieaxact=cpu_elegido.socket,
                stock__gt=0
            )
        else:
            productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='placa madre', stock__gt=0)

    elif paso_actual == 'memoria_ram':
            mother_id = armado.get('placa_madre')
            mother_elegida = Producto.objects.filter(id=mother_id).first() if mother_id and mother_id != 'omitido' else None
    
            if mother_elegida and mother_elegida.tipo_memoria:
                productos_filtrados = Producto.objects.filter(
                    categoria__nombre__iexact='memoria ram',
                    socket__ieaxact=mother_elegida.tipo_memoria,
                    stock__gt=0
                )
            else:
                productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='memoria ram', stock__gt=0)

    elif paso_actual == 'tarjeta_grafica':
        productos_filtrados = Producto.objects.filter(categoria__nombre__iexact='tarjetagrafica', stock__gt=0)

    #Paginacion reutilizada de tienda,html
    paginator = Paginator(productos_filtrados, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    titulos = {
        'proceasdor': 'Procesador',
        'placa_madre': 'Placa Madre',
        'memoria_ram': 'Memoria RAM',
        'tarjeta_grafica': 'Tarjeta Gráfica',
        'finalizado': '¡Armado Completado!',
    }

    #verificamos si hay accion tomada, para poder reiniciar
    tiene_progreso = any(val is not None for val in armado.values())
    #verificamos si eligio un producto para habilitar compra
    tiene_productos_reales = any(val is not None and val != 'omitido' for val in armado.values())

    context = {
        'paso_actual': paso_actual,
        'paso_titulo': titulos.get(paso_actual, paso_actual),
        'armado_completo': armado_completo,
        'tiene_progreso': tiene_progreso,
        'tiene_productos_reales': tiene_productos_reales,
        'productos': page_obj,
        'armado': armado,
        'cpu_elegido': Producto.objects.filter(id=armado.get('procesador')).first() if armado.get('procesador') not in [None, 'omitido'] else None,
        'mother_elegida': Producto.objects.filter(id=armado.get('placa_madre')).first() if armado.get('placa_madre') not in [None, 'omitido'] else None,
        'ram_elegida': Producto.objects.filter(id=armado.get('memoria_ram')).first() if armado.get('memoria_ram') not in [None, 'omitido'] else None,
        'gpu_elegida': Producto.objects.filter(id=armado.get('tarjeta_grafica')).first() if armado.get('tarjeta_grafica') not in [None, 'omitido'] else None,
    }

    return render(request, 'armado/asistente.html', context)

def seleccionar_componente(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categoria = producto.categoria.nombre.lower()

    armado = request.session.get('carrito_armado', {})

    if 'procesador' in categoria:
        armado['procesador'] = producto.id
        armado['placa_madre'] = None
        armado['memoria_ram'] = None
    elif 'placa madre' in categoria:
        armado['placa_madre'] = producto.id
        armado['memoria_ram'] = None
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
    request.session['carrito_armado'] = {
        'procesador': None,
        'placa_madre': None,
        'memoria_ram': None,
        'tarjeta_grafica': None,
    }
    request.session.modified = True
    return redirect('asistente_armado')