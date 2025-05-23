from rest_framework import serializers
from usuario.models import Usuario, Rol, Descripción_rol

class usuarioserializers(serializers.ModelSerializers):
    class Meta:
        models = Usuario
        fields = ['documento', 'nombre', 'correo', 'Telefono','rol']

class Rolserializers(serializers.ModelSerializers):
    class Meta:
        models = Rol
        fields = ['id', 'nombreRol', 'descripcionRol', 'reportes']

class Descripción_rolserializers(serializers.ModelSerializers):
    class Meta:
        models = Descripción_rol
        fields = ['id', 'sector']