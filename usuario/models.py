from django.db import models


class Usuario(models.Model):
    documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField( max_length=254)
    telefono = models.IntegerField()
    ROLE_APRENDIZ= "Aprendiz"
    ROLE_INSTRUCTOR= "Instructor"
    ROLE_ADMIN= "Administrador"
    ROLE_MANTENIMIENTO= "Personal de mantenimiento"

    ROLE_CHOICES=[
        (ROLE_APRENDIZ, "Aprendiz"),
        (ROLE_INSTRUCTOR, "Instructor"),
        (ROLE_ADMIN, "Administrador"),
        (ROLE_MANTENIMIENTO, "Personal de mantenimiento")
    ]
    rol= models.CharField(
        max_length=25,
        choices=ROLE_CHOICES,
        default=ROLE_APRENDIZ,
        help_text="Define el nivel de acceso del usuario"
    )
    USERNAME_FIELD = "Documento"
    REQUIRED_FIELDS=["username"]
    def __str__(self):
        return self.documento().__str__()


