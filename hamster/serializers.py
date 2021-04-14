from django.contrib.auth.models import User, Group
from hamster.models import Institucion, Funcionario, Beneficiario, Contribucion
from rest_framework import serializers



# Clases para serializar los modelos de datos

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__' #['id', 'username', 'email', 'is_staff']


class InstitucionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Institucion
		fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):

	#institucion = serializers.StringRelatedField(many=False)
	institucion = InstitucionSerializer(read_only=True)
	
	class Meta:
		model = Funcionario
		fields = '__all__'



class ContribucionSerializer2(serializers.ModelSerializer):

	class Meta:
		model = Contribucion
		fields = ['id', 'fecha', 'concepto', 'monto']



class BeneficiarioSerializer(serializers.ModelSerializer):
	
	contribuciones = ContribucionSerializer2(many=True, read_only=True)

	class Meta:
		model = Beneficiario
		fields = '__all__'



class ContribucionSerializer(serializers.ModelSerializer):

	digitador = serializers.ReadOnlyField(source='digitador.email')
	funcionario = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all())
	beneficiario = serializers.PrimaryKeyRelatedField(queryset=Beneficiario.objects.all())

	class Meta:
		model = Contribucion
		fields = '__all__'




		