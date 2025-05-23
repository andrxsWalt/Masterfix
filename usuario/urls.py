from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RolViewSet, DescripcionRolViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'descripciones', DescripcionRolViewSet)

urlpatterns = [
    path('', include(router.urls)),
]