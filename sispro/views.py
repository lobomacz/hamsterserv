from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db import transaction
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_gis import filters
from rest_framework.filters import SearchFilter
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from sispro.permissions import IsOwnerOrReadOnly
from sispro.serializers import *
from sispro.models import *
import datetime
import json


# Create your views here.


# Mixins

# Mixin de hitcount
class RestHitMixin(HitCountMixin):

	def dispatch(self, request, *args, **kwargs):
		response = super(RestHitMixin, self).dispatch(request, *args, **kwargs)

		if hasattr(self, "action") and self.action not in ["retrieve"]:
			return response

		if hasattr(self, "get_queryset") and callable(getattr(self, "get_queryset")):
			opts, u = self.get_queryset().model._meta, request.user

			def hit_action():
				ctype = ContentType.objects.get(app_label=opts.app_label, model=opts.model)

				hitcount, created = HitCount.objects.get_or_create(content_type=ctype, object_pk=kwargs["pk"])

				self.hit_count(request, hitcount)

			transaction.on_commit(hit_action)

		return response

	def get_serializer_class(self):
		class RestHitSerializer(super(RestHitMixin, self).get_serializer_class()):
			def to_representation(cls, instance):
				response = super(RestHitSerializer, cls).to_representation(instance)

				def get_hits(obj):
					try:
						return HitCount.objects.get_for_object(obj).hits
					except: #noqa
						return 0

				response.update({"hits":get_hits(instance)})

				return response

		return RestHitSerializer



# Mixin de digitador
class DigitadorMixin():
	def perform_create(self, serializer):
		serializer.save(digitador=self.request.user)


# Vistas principales

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





