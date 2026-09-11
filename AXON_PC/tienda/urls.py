from django.urls import path
from . import views

urlpatterns = [
    path('tienda/', views.tienda, name='tienda'),
    path('producto/', views.producto, name='producto'),
]