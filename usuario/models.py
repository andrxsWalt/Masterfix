from django.db import models


#La clase usuario define qué componentes tienen las personas que se pueden registrar en la plataforma, como lo son instructores, adminisitradores y operadores
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

# -----------------------------PROYECTO RIAÑO (Microstock)-----------------------------------
# Modelo que representa un rol dentro del sistema (por ejemplo: administrador, vendedor, etc.)
class Rol(models.Model):
    # Campo de texto que almacena el nombre del rol, limitado a 20 caracteres.
    nombre = models.CharField(max_length=20)

    # Campo de texto que describe brevemente el rol, con un máximo de 100 caracteres.
    descripcion = models.CharField(max_length=100)

    # Método que devuelve el nombre del rol al representarlo como texto (útil en el panel de administración).
    def __str__(self):
        return self.nombre


# Modelo que representa a una persona usuaria del sistema, vinculada a un rol específico.
class persona(models.Model):
    # Nombre completo de la persona, hasta 50 caracteres.
    nombre = models.CharField(max_length=50)

    # Correo electrónico de la persona. Se valida automáticamente como un email.
    correo = models.EmailField(max_length=60)

    # Contraseña de acceso. Se guarda como texto, aunque en un sistema real se recomienda cifrarla.
    contraseña = models.CharField(max_length=20)

    # Relación con el modelo Rol. Cada persona tiene asignado un único rol.
    # Si se elimina un rol, también se eliminan las personas que lo tengan asignado.
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    # Representación textual del modelo, devuelve el nombre de la persona.
    def __str__(self):
        return self.nombre

