from rest_framework import serializers
from usuario.models import Usuario, Rol, DescripciónRol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        models = Usuario
        fields = ['documento', 'nombre', 'correo', 'Telefono','rol']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        models = Rol
        fields = ['id', 'nombreRol', 'descripcionRol', 'reportes']

class DescripciónRolSerializer(serializers.ModelSerializer):
    class Meta:
        models = DescripciónRol
        fields = ['id', 'sector']