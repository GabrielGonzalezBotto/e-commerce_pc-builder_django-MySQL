from django.contrib import admin
from .models import Categoria, Producto, EspecificacionTecnica, Review

# Register your models here.
class EspecificacionTecnicaInline(admin.TabularInline):
    model = EspecificacionTecnica
    extra = 3

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock') #Columnas generales
    list_display_links = ('id', 'nombre')
    list_filter = ('categoria',) #Filtro derecho lateral por componente
    search_fields = ('nombre', 'descripcion') #Buscador de texto en le panel
    inlines = [EspecificacionTecnicaInline] #Inyecta la carga tecnica en le  preducto

#Regsitro para Categoria y Opinioines
admin.site.register(Categoria)
admin.site.register(Review)