from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from hamster.serializers import *
from hamster.models import *
from hamster.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 



# Create your views here.

class ContribucionViewSet(viewsets.ModelViewSet):

	""" 
	Este viewset gestiona las operaciones CRUD de Contribuciones
	""" 

	queryset = Contribucion.objects.all()
	serializer_class = ContribucionSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(digitador=self.request.user)


''' 
class ListaContribuciones(generics.ListCreateAPIView):

	"""
	Vista que obtiene la lista de contribuciones
	de la base de datos y devuelve un objeto JSON 
	del resultado del queryset o crea una nueva entrada
	si el método usado es POST
	"""

	queryset = Contribucion.objects.all()
	serializer_class = ContribucionSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(digitador=self.request.user)



class DetalleContribucion(generics.RetrieveUpdateDestroyAPIView):

	"""
	Vista que gestiona el detalle de la contribución
	incluyendo funciones para actualizar y eliminar con los 
	métodos PUT y DELETE
	"""

	queryset = Contribucion.objects.all()
	serializer_class = ContribucionSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
'''		
		
class BeneficiarioViewSet(viewsets.ModelViewSet):

	"""
	Este viewset gestiona las operaciones CRUD de Beneficiario
	"""

	queryset = Beneficiario.objects.all()
	serializer_class = BeneficiarioSerializer
	permission_classes = [permissions.IsAuthenticated]


''' 
class ListaBeneficiarios(generics.ListCreateAPIView):

	"""
	Vista que obtiene la lista de beneficiarios
	de la base de datos y devuelve un objeto JSON 
	del resultado del queryset o crea una nueva entrada
	si el método usado es POST
	"""
	
	queryset = Beneficiario.objects.all()
	serializer_class = BeneficiarioSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class DetalleBeneficiario(generics.RetrieveUpdateDestroyAPIView):

	"""
	Vista que gestiona el detalle del beneficiario
	incluyendo funciones para actualizar y eliminar con los 
	métodos PUT y DELETE
	"""

	queryset = Beneficiario.objects.all()
	serializer_class = BeneficiarioSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

''' 
				

class FuncionarioViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Este viewset va a gestionar las operaciones CRUD de Funcionarios
	""" 
	queryset = Funcionario.objects.all()
	serializer_class = FuncionarioSerializer
	permission_classes = [permissions.IsAuthenticated]


''' 

class ListaFuncionarios(generics.ListAPIView):

	queryset = Funcionario.objects.all() 
	serializer_class = FuncionarioSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class DetalleFuncionario(generics.RetrieveAPIView):

	queryset = Funcionario.objects.all()
	serializer_class = FuncionarioSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
''' 



class InstitucionViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Institucion.objects.all()
	serializer_class = InstitucionSerializer
	permission_classes = [permissions.IsAuthenticated]
	


# NO SE USA
class UserDetail(generics.RetrieveAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer
	


class UserLogin(APIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]


	def post(self, request, format=None):

		print(request.data)
		uname = request.data['username']
		pword = request.data['password']

		user = authenticate(username=uname, password=pword)
		if user is not None:
			serializer = UserSerializer(user)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








		


		
