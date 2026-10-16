from django.urls import path
from . import views

urlpatterns = [
    path('tienda/', views.tienda, name='tienda'),
    path('producto/<int:pk>/', views.producto, name='producto'),
    path('favorito/toggle/<int:producto_id>/', views.toggle_favorito, name='toggle_favorito'),
]