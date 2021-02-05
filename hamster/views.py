#from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import FormView 
from django.http import JsonResponse, HttpResponseForbidden
from django.core import serializers
from hamster.models import Contribucion, Beneficiario
from hamster.forms import FormContribucion, FormBeneficiario

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
	model = Contribucion

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
	model = Contribucion

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

	form_class = FormContribucion
	model = Contribucion
	
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
	
	model = Beneficiario

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
	model = Beneficiario

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
	
	form_class = FormBeneficiario
	model = Beneficiario

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
		

		


		
