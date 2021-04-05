from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from hamster.serializers import *
from hamster.models import *
from hamster.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import action



# Create your views here.

class ContribucionViewSet(viewsets.ModelViewSet):

	""" 
	Este viewset gestiona las operaciones CRUD de Contribuciones
	""" 

	queryset = Contribucion.objects.all()
	serializer_class = ContribucionSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

	@action(detail=True)
	def por_beneficiario(self, request, pk=None):
		contribuciones = self.get_queryset().filter(beneficiario=pk)
		serializer = self.get_serializer(contribuciones, many=True)
		return Response(serializer.data)


	def perform_create(self, serializer):
		serializer.save(digitador=self.request.user)


		
class BeneficiarioViewSet(viewsets.ModelViewSet):

	"""
	Este viewset gestiona las operaciones CRUD de Beneficiario
	"""

	queryset = Beneficiario.objects.all()
	serializer_class = BeneficiarioSerializer
	permission_classes = [permissions.IsAuthenticated]

				

class FuncionarioViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Este viewset va a gestionar las operaciones CRUD de Funcionarios
	""" 
	queryset = Funcionario.objects.all()
	serializer_class = FuncionarioSerializer
	permission_classes = [permissions.IsAuthenticated]




class InstitucionViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Institucion.objects.all()
	serializer_class = InstitucionSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	


class UserLogin(APIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]


	def post(self, request, format=None):

		uname = request.data['username']
		pword = request.data['password']

		user = authenticate(username=uname, password=pword)
		if user is not None:
			serializer = UserSerializer(user)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








		


		
