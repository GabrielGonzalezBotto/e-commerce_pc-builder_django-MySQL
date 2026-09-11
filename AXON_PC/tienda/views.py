from django.shortcuts import render

# Create your views here.
def tienda(request):
    #render toma el request y el HTML para mostrar
    return render(request, 'tienda/tienda.html')

def producto(request):
    #render toma el request y el HTML para mostrar
    return render(request, 'tienda/producto.html')
