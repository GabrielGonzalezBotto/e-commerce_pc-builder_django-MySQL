from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #Ruta principal, llama a la vista Index
    path('contacto/', views.contacto, name='contacto'), #ruta contacto, llama a la vista contacto
]