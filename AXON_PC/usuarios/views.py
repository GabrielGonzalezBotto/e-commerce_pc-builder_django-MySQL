from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages

# Create your views here.

#REGISTRO DE USUARIO
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('tienda')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

#INICIAR SESION
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('tienda')
        else:
            print(form.errors)
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

#CERRAR SESION
def logout_view(request):
    logout(request)
    return redirect('login')

#ACCEDER A PERFIL LOGUEADO
@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')
