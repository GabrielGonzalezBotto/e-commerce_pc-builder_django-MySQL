from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.asistente_armado, name='asistente_armado'),
    path('seleccionar/<int:producto_id>/', views.seleccionar_componente, name='seleccionar_componente'),
    path('reiniciar/', views.reiniciar_armado, name='reiniciar_armado'),
]  