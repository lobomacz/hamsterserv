from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from sispro.models import *

# Serializadores de modelos


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']


class sTecnico(serializers.ModelSerializer):

	class Meta:
		model = Tecnico
		fields = ['cedula', 'nombres', 'apellidos']


class sPrograma(serializers.ModelSerializer):

	class Meta:
		model = Programa
		fields = '__all__'



class sProyecto(serializers.ModelSerializer):

	class Meta:
		model = Proyecto
		fields = ['id', 'codigo', 'nombre', 'acronimo']


class sBono(serializers.ModelSerializer):

	class Meta:
		model = Bono
		fields = '__all__'



class sProtagonistaBono(GeoFeatureModelSerializer):

	protagonista = serializers.PrimaryKeyRelatedField(many=False)
	bono = serializers.PrimaryKeyRelatedField(many=False)
	proyecto = serializers.StringRelatedField(many=False)
	digitador = UserSerializer(many=False, read_only=True)

	class Meta:
		model = ProtagonistaBono
		geo_field = 'location'
		fields = '__all__'


class sProtagonista(serializers.ModelSerializer):

	comunidad = serializers.StringRelatedField(many=False)
	etnia = serializers.StringRelatedField(many=False)
	bonos = sProtagonistaBono(many=True, read_only=True)

	class Meta:
		model = Protagonista
		fields = '__all__'


class sKeyProtagonistaBono(serializers.ModelSerializer):

	protagonista = serializers.StringRelatedField(many=False, read_only=True)
	bono = serializers.StringRelatedField(many=False, read_only=True)

	class Meta:
		model = ProtagonistaBono
		fields = ['id', 'protagonista', 'bono']


class sCapitalizacion(serializers.ModelSerializer):

	p_bono = serializers.PrimaryKeyRelatedField(many=False)
	articulo = serializers.PrimaryKeyRelatedField(many=False)
	unidad = serializers.PrimaryKeyRelatedField(many=False)
	digitador = UserSerializer(many=False, read_only=True)

	class Meta:
		model = Capitalizacion
		fields = '__all__'

class sProtagonistaString(serializers.ModelSerializer):

	class Meta:
		model = Protagonista
		fields = ['cedula', 'nombres', 'apellidos']



class sCapacitacion(serializers.ModelSerializer):

	protagonista = serializers.PrimaryKeyRelatedField(many=False)
	bono = serializers.PrimaryKeyRelatedField(many=False)
	protagonista_str = sProtagonistaString(many=False, read_only=True)

	class Meta:
		model = Capacitacion
		fields = '__all__'


class sAporte(serializers.ModelSerializer):

	p_bono = serializers.PrimaryKeyRelatedField(many=False)

	class Meta:
		model = AporteBono
		fields = '__all__'