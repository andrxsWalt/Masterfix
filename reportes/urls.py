from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportesViewSet, EstadoReporteViewSet

router = DefaultRouter()
router.register(r'reportes', ReportesViewSet)
router.register(r'estados', EstadoReporteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]