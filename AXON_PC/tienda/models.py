from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"

class EspecificacionTecnica(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='especificaciones')
    clave = models.CharField(max_length=50, help_text="Ej: Socket, Tipo de Memoria, Watts, Formato")
    valor =  models.CharField(max_length=100, help_text="Ej: AM4, DDR4, 65W, Micro-ATX")

    class Meta:
        verbose_name = "Especificación Técnica"
        verbose_name_plural = "Especificaciones Técnicas"

    def __str__(self):
        return f"{self.producto.nombre} -> {self.clave}: {self.valor}"


class Review(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='reviews')
    ususario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comentario = models.TextField()
    stars = models.IntegerField(choices=[(i,i) for i in range(1,6)], default=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = 'review'
    verbose_name_plural = 'reviews'
    ordering = ['-fecha_creacion']

def __str__(self):
    return f"Reseña de {self.usuario.username} para {self.producto.nombre}"