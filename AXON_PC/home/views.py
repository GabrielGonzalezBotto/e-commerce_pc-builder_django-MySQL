from django.shortcuts import render

# Create your views here.

#vista pagina principal
def index(request):
    #render toma el request y el HTML para mostrar
    return render(request, 'home/index.html')

def contacto(request):
    return render(request, 'home/contacto.html')
