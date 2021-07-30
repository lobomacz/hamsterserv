from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from suir.views import *


#  Creación del DefaultRouter para que maneje
#  las rutas de los ViewSets

# router = DefaultRouter()

#  Registramos los ViewSets con su segmento de la URL

# router.register(r'anuncios', AnuncioViewSet)
# router.register(r'tablas', TablaViewSet)
# router.register(r'indicadores', IndicadorViewSet)
# router.register(r'enlaces', LinkExternoViewSet)
# router.register(r'publicaciones', PublicacionViewSet)

urlpatterns = [
	# path('', include(router.urls)),
]