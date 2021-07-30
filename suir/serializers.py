from suir.models import *
from rest_framework import serializers


# Clases para serializar modelos de datos en la API

class sAnuncio(serializers.ModelSerializer):

	class Meta:
		model = Anuncio 
		fields = '__all__'


class sContacto(serializers.ModelSerializer):

	class Meta:
		model = Contacto
		fields = '__all__'
		depth = 1


class sTabla(serializers.ModelSerializer):

	class Meta:
		model = Tabla 
		fields = '__all__'
		depth = 1


class sEntidad(serializers.ModelSerializer):

	class Meta:
		model = Entidad 
		fields = '__all__'
		depth = 1



class sValorIndicador(serializers.ModelSerializer):

	class Meta:
		model = ValorIndicador 
		fields = '__all__'
		depth = 1



class sIndicador(serializers.ModelSerializer):

	valores = sValorIndicador(many=True, read_only=True)

	class Meta:
		model = Indicador 
		exclude = ['estado', 'version', 'seguimiento', 'activo', 'creador']  # fields = '__all__'
		depth = 1


class sLinkExterno(serializers.ModelSerializer):

	class Meta:
		model = LinkExterno 
		fields = '__all__'


class sThumbPublicacion(serializers.ModelSerializer):

	class Meta:
		model = Publicacion
		fields = ['id', 'titulo', 'portada', 'tipo']


class sPublicacion(serializers.ModelSerializer):

	class Meta:
		model = Publicacion 
		fields = '__all__'
		depth = 1