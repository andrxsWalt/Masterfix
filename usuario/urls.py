from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView,
    RolListCreateView, RolRetrieveUpdateDestroyView,
    DescripcionRolListCreateView, DescripcionRolRetrieveUpdateDestroyView
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioListCreateView)
router.register(r'roles', RolListCreateView)
router.register(r'descripciones', DescripcionRolListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]