from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import View, FormView 
from django.http import JsonResponse, HttpResponseForbidden
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from . import models
from . import forms as frm

# Create your views here.
class JsonResponseMixin:

	"""
	Clase Mixin para devolver una repuesta JSON
	"""

	def render_to_json_response(self, context, **response_kwargs):
		"""
		Devuelve una respuesta convirtiendo el objeto context a JSON
		"""
		return JsonResponse(self.get_data(context), **response_kwargs)


	def get_data(self, context):
		"""
		Devuelve un objeto convertido a JSON
		"""
		data = serializers.serialize('json', context)
		return data



class ListaContribuciones(JsonResponseMixin, ListView):

	"""
	Vista que obtiene la lista de contribuciones
	de la base de datos y devuelve un objeto JSON 
	del resultado del queryset
	"""

	model = models.Contribucion

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			return super().get(request, *args, **kwargs)

	def render_to_response(self, context, **response_kwargs):
		
		return self.render_to_json_response(context, **response_kwargs)


class DetalleContribucion(JsonResponseMixin, DetailView):

	"""
	Vista que devuelve el detalle de la contribución
	"""

	model = models.Contribucion

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			return super().get(request, *args, **kwargs)


	def render_to_response(self, context, **response_kwargs):

		return self.render_to_json_response(context, **response_kwargs)
	
		
	
class FormContribucionView(SingleObjectMixin, FormView):

	"""
	Procesa los datos del formulario y guarda el modelo de datos.
	Despuúes, redirige a la url del detalle del registro.
	"""

	form_class = frm.FormContribucion
	model = models.Contribucion
	
	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			self.object = self.get_object()
			return super().post(request, *args, **kwargs)

	def get_success_url(self):

		return self.object.get_absolute_url()


#PROBABLEMENTE NO SE USE
@method_decorator(ensure_csrf_cookie, name='dispatch')
class NuevaContribucion(View):

	"""
	Procesa los datos del formulario con el metodo post
	"""

	def post(self, request, *args, **kwargs):
		view = FormContribucionView.as_view()
		return view(request, *args, **kwargs)



@method_decorator(ensure_csrf_cookie, name='dispatch')
class EditContribucion(View):

	"""
	Devuelve un objeto JSON con el metodo get
	y procesa los datos del formulario con el metodo post
	"""

	def get(self, request, *args, **kwargs):
		view = DetalleContribucion.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = FormContribucionView.as_view()
		return view(request, *args, **kwargs)
		

class ListaBeneficiarios(JsonResponseMixin, ListView):

	"""
	Devuelve un objeto JSON con la lista de Beneficiarios
	"""
	
	model = models.Beneficiario

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			return super().get(request, *args, **kwargs)

	def render_to_response(self, context, **response_kwargs):

		return self.render_to_json_response(context, **response_kwargs)


class DetalleBeneficiario(JsonResponseMixin, DetailView):

	"""
	Devuelve un objeto JSON correspondiente al Beneficiario
	"""

	model = models.Beneficiario

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			return super().get(request, *args, **kwargs)

	def render_to_response(self, context, **response_kwargs):

		return super().render_to_json_response(context, **response_kwargs)
		


class FormBeneficiarioView(SingleObjectMixin, FormView):

	"""
	Asegura el envío de la cookie con el token csrf y
	procesa los datos de formulario para guardar o editar
	modelos de dato de Beneficiarios.
	"""
	
	form_class = frm.FormBeneficiario
	model = models.Beneficiario

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			self.object = self.get_object()
			return super().post(request, *args, *kwargs)

	def get_success_url(self):

		return self.object.get_absolute_url()


@method_decorator(ensure_csrf_cookie, name='dispatch')
class EditBeneficiario(View):
	
	"""
	Garantiza un objeto JSON con el token csrf en el metodo get
	y procesa los datos de formulario en el metodo post.
	Hace el llamado a otras vistas para cada metodo (get, post) por 
	separado.
	"""
	
	def get(self, request, *args, **kwargs):
		view = DetalleBeneficiario.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = FormBeneficiarioView.as_view()
		return view(request, *args, **kwargs)
		
class UserData(JsonResponseMixin, View):

	model_class = User

	def get(self, request, *args, **kwargs):
		
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			user = get_object_or_404(model_class, pk=request.user.id)
			context = {'usuario':user}
			return self.render_to_json_response(context)



@method_decorator(ensure_csrf_cookie, name='dispatch')
class UserLogin(JsonResponseMixin, View):

	form_class = frm.FormLogin
	model_class = User

	def get(self, request, *args, **kwargs):
		context = {'usuario':self.model_class()}
		return self.render_to_json_response(context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			credentials = form.cleaned_data
			user = authenticate(username=credentials['username'], password=credentials['password'])
			if user is not None:
				login(request, user)
				context = {'usuario':user}
				return self.render_to_json_response(context)
			else:
				return HttpResponseForbidden()


class ListaFuncionarios(JsonResponseMixin, ListView):

	model = models.Funcionario 

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			return super().get(request, *args, **kwargs)

	def render_to_response(self, context, **response_kwargs):

		return self.render_to_json_response(context, **response_kwargs)


class ListaInstituciones(ListaFuncionarios):

	model = models.Institucion 




		


		
