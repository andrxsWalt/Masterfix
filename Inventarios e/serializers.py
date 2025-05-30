from rest_framework import serializers
from .models import empresa, categoria, producto

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'
