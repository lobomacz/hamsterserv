from django.urls import include, path
#from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from hamster.views import *

# Creamos un router para los viewsets utilizados en la API
router = DefaultRouter()
router.register(r'instituciones', InstitucionViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)
router.register(r'contribuciones', ContribucionViewSet)


urlpatterns = [
	path('auth/', UserLogin.as_view(), name='user_login'),
	path('', include(router.urls))
#	path('contribuciones/', include([
#			path('', ListaContribuciones.as_view(), name='lista_contribuciones'),
#			path('<int:pk>/', DetalleContribucion.as_view(), name='detalle_contribucion'),
#		])),
#	path('beneficiarios/', include([
#			path('', ListaBeneficiarios.as_view(), name='lista_beneficiarios'),
#			path('<str:pk>/', DetalleBeneficiario.as_view(), name='detalle_beneficiario'),
#		])),
#	path('funcionarios/', include([
#			path('', ListaFuncionarios.as_view(), name='lista_funcionarios'),
#			path('<int:pk>/', DetalleFuncionario.as_view(), name='detalle_funcionario'),
#		])),
#	path('instituciones/', ListaInstituciones.as_view(), name='lista_instituciones'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)