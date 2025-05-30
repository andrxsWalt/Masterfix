from django.db import models

class carrito(models.Model):
    cliente = models.CharField(max_length=50)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente

class producto(models.Model):
    nombre_pro = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    cantidad_pedido = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_pro    
# Create your models here.
