from django import forms
from django.forms import Form, ModelForm
from suir.models import Publicacion, ValorIndicador

# Clases de formularios


# class LoginForm(Form):
# 	"""
# 	Formulario de validación de usuarios
# 	"""
# 	username = models.CharField("Nombre de Usuario", max_length=25)
# 	contrasena = models.CharField("Contraseña", min_length=8, widget=forms.PasswordInput)




class PublicacionForm(ModelForm):

	class Meta:
		model = Publicacion
		exclude = ['slug', 'autor', 'tipo', 'publicado']


class ValorIndicadorForm(ModelForm):

	class Meta:
		model = ValorIndicador
		exclude = ['digitador','supervisor']
		labels = {
			'indicador':'Indicador',
			'entidad':'Entidad',
			'comunidad':'Comunidad',
			'rango_edad':'Rango de edad',
			'estado':'Estado de publicación',
		}