from django.db import models

# Create your models here.
class Usuario(models.Model):
    documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField( max_length=254)
    telefono = models.IntegerField()
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.documento().__str__()


class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)
    descripcionRol = models.ForeignKey('DescripciónRol', on_delete=models.CASCADE)
    reportes = models.ForeignKey('reportes.Reportes', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreRol().__str__()

class DescripciónRol(models.Model):
    sector = models.CharField(max_length=100)
    def __str__(self):
        return self.sector().__str__()