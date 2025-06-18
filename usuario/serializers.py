from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['documento', 'nombre', 'correo', 'telefono','rol']
        