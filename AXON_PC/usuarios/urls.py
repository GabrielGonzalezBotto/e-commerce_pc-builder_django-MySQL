from django.urls import path
from . import views

urlpatterms = [
    path('registro/', views.resgistro_view, name='registro'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
]