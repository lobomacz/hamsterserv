from django.urls import include, path
from rest_framework.routers import DefaultRouter
from sispro.views import *


# Creamos un router para la API

router = DefaultRouter()
router.register(r'programas', ProgramasViewSet)
router.register(r'proyectos', ProyectosViewSet)
router.register(r'protagonistas', ProtagonistasViewSet)
router.register(r'bonos', ProtagonistasBonosViewSet)
router.register(r'planes', PlanesInversionViewSet)
router.register(r'capitalizacion', CapitalizacionViewSet)
router.register(r'aportes', AporteViewSet)
router.register(r'capacitacion', CapacitacionViewSet)

urlpatterns = [
	path('auth/', LoginView.as_view(), name='sispro_login'),
	path('', include(router.urls)),
]
