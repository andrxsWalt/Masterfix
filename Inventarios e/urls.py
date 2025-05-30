from django.urls import path
from .views import (
    EmpresaListCreateView, EmpresaRetrieveUpdateDestroyView,
    CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView,
    ProductoListCreateView, ProductoRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Empresa endpoints
    path('empresas/', EmpresaListCreateView.as_view(), name='empresa-list-create'),
    path('empresas/<int:id>/', EmpresaRetrieveUpdateDestroyView.as_view(), name='empresa-detail'),

    # Categoria endpoints
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:id>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),

    # Producto endpoints
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:id>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-detail'),
]