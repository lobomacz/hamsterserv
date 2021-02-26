from django.urls import include, path
from hamster.views import *

urlpatterns = [
	path('auth/', include([
			path('user/', UserData.as_view(), name='user_data'),
			path('login/', UserLogin.as_view(), name='user_login'),
		])),
	path('contribuciones/', include([
			path('lista/', ListaContribuciones.as_view(), name='lista_contribuciones'),
			path('<int:pk>/', DetalleContribucion.as_view(), name='detalle_contribucion'),
			path('nueva/', EditContribucion.as_view(), name='nueva_contribucion'),
			path('<int:pk>/edit/', EditContribucion.as_view(), name='edit_contribucion'),
		])),
	path('beneficiarios/', include([
			path('lista/', ListaBeneficiarios.as_view(), name='lista_beneficiarios'),
			path('<str:pk>/', DetalleBeneficiario.as_view(), name='detalle_beneficiario'),
			path('nuevo/', EditBeneficiario.as_view(), name='nuevo_beneficiario'),
			path('<str:pk>/edit/', EditBeneficiario.as_view(), name='edit_beneficiario'),
		])),
	path('lista/', include([
			path('funcionarios/', ListaFuncionarios.as_view(), name='lista_funcionarios'),
			path('instituciones/', ListaInstituciones.as_view(), name='lista_instituciones'),
			
		])),
]