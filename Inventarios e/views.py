from rest_framework.response import Response
from rest_framework import generics
from .models import empresa, categoria, producto
from .serializers import EmpresaSerializer, CategoriaSerializer, ProductoSerializer

# Empresa Views
class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = empresa.objects.all()
    serializer_class = EmpresaSerializer
    lookup_field = 'id'

# Categoria Views
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'id'

# Producto Views
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id'
# Create your views here.
