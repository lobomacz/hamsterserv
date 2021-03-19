from django.contrib.auth.models import User, Group
from hamster.models import Institucion, Funcionario, Beneficiario, Contribucion
from rest_framework import serializers



# Clases para serializar los modelos de datos

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'is_staff']


class InstitucionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Institucion
		fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Funcionario
		fields = '__all__'


class BeneficiarioSerializer(serializers.ModelSerializer):
	contribuciones = serializers.PrimaryKeyRelatedField(many=True, queryset=Contribucion.objects.all())

	class Meta:
		model = Beneficiario
		fields = '__all__'

class ContribucionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contribucion
		fields = '__all__'
		