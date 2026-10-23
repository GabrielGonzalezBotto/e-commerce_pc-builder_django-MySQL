from django.urls import path
from . import views

urlpatterns = [
    path('tienda/', views.tienda, name='tienda'),
    path('producto/<int:pk>/', views.producto, name='producto'),
    path('favorito/toggle/<int:producto_id>/', views.toggle_favorito, name='toggle_favorito'),
    path('review/eliminar/<int:review_id>/', views.eliminar_review, name='eliminar_review'),
    path('review/editar/<int:review_id>/', views.editar_review, name='editar_review'),
]