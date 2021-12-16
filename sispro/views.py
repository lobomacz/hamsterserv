from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.db.models import Q
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_gis import filters
from rest_framework.filters import SearchFilter
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View 
# from django.views.generic.base import TemplateView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, FormView
from django.db import transaction
from sispro.permissions import IsOwnerOrReadOnly
from sispro.serializers import *
from sispro.models import *
#from sispro.forms import *
import datetime
import json


# Create your views here.


# Vistas principales

# Mixin de digitador
class DigitadorMixin():
	def perform_create(self, serializer):
		serializer.save(digitador=self.request.user)


# Vista de ingreso de usuarios(login)
class LoginView(APIView):

	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]
	queryset = User.objects.all()

	def post(self, request, format=None):

		uname = request.data['nombreusuario']
		passwd = request.data['contrasena']

		user = authenticate(uname, passwd)

		if user is not None:
			serializer = UserSerializer(user)
			return Response(serializer.data, status.HTTP_200_OK)
		else:
			return Response(json.dumps({'mensaje':'¡Credenciales Incorrectas!'}), status.HTTP_400_BAD_REQUEST)



# ViewSet de Programas
class ProgramasViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Programa.objects.all()
	serializer_class = sPrograma
	filter_backends = [SearchFilter]
	search_fields = ['nombre','codigo']
	permission_classes = [permissions.AllowAny]



# ViewSet de Proyectos
class ProyectosViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Proyecto.objects.all()
	serializer_class = sProyecto
	filter_backends = [SearchFilter]
	search_fields = ['nombre', 'codigo']
	permission_classes = [permissions.AllowAny]



# ViewSet de Protagonistas
class ProtagonistasViewSet(viewsets.ModelViewSet):

	queryset = Protagonista.objects.all()
	serializer_class = sProtagonista
	filterset_fields = ['cedula']



# ViewSet de Bonos entregados
class ProtagonistasBonosViewSet(DigitadorMixin, viewsets.ModelViewSet):

	queryset = ProtagonistaBono.objects.filter(bono__tipo__elemento='bono')
	filterset_fields = ['protagonista__cedula']
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
	serializer_class = sProtagonistaBono



# ViewSet de Planes de Inversión entregados
class PlanesInversionViewSet(ProtagonistasBonosViewSet):

	queryset = ProtagonistaBono.objects.filter(bono__tipo__elemento='plan de inversion')

	

# ViewSet de Capitalizaciones de Planes de Inversión
class CapitalizacionViewSet(DigitadorMixin, viewsets.ModelViewSet):

	queryset = Capitalizacion.objects.all()
	serializer_class = sCapitalizacion
	permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
	filterset_fields = ['p_bono__protagonista__cedula']



# ViewSet de Aporte a Planes de inversión.
class AporteViewSet(CapitalizacionViewSet):

	queryset = Aporte.objects.filter(p_bono__bono__tipo__elemento='plan de inversion')
	serializer_class = sAporte
	filterset_fields = ['p_bono__protagonista__cedula']




# ViewSet de Capacitaciones
class CapacitacionViewSet(CapitalizacionViewSet):

	queryset = Capacitacion.objects.all()
	serializer_class = sCapacitacion
	filterset_fields = ['protagonista__cedula']





