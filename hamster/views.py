from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.sessions.models import Session
from django.conf import settings
from importlib import import_module
from . import models
from . import forms as frm
import json
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

# Create your views here.
class JsonResponseMixin:

	"""
	Clase Mixin para devolver una repuesta JSON
	"""

	def render_to_json_response(self, context, **response_kwargs):
		"""
		Devuelve una respuesta convirtiendo el objeto context a JSON
		"""
		return JsonResponse(context, **response_kwargs)


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

	def get_queryset(self):
		self.queryset = self.model.objects.annotate(contrib_count=Count('contribucion'))
		return self.queryset

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

	def get_queryset(self):
		self.queryset = self.model.objects.annotate(contrib_count=Count('contribucion'))
		return self.queryset

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

		
@method_decorator(csrf_exempt, name='dispatch')
class UserSession(JsonResponseMixin, View):

	model_class = User

	def post(self, request, *args, **kwargs):
		data = json.loads(request.body)
		sesion = Session.objects.get(pk=data['sessionid'])
		s = sesion.get_decoded()
		if s['_auth_user_id'] == data['userid']:
			user = self.model_class.objects.get(pk=data['userid'])
			context = {'expire_date':sesion.expire_date}
			if user is not None:
				user_dict = model_to_dict(user, fields=['id', 'username', 'first_name', 'last_name', 'email'])
				context['usuario'] = user_dict
			return self.render_to_json_response(context)
		else:
			return HttpResponseForbidden()


@method_decorator(csrf_exempt, name='dispatch')
class UserLogout(JsonResponseMixin, View):
	
	def post(self, request, *args, **kwargs):
		data = json.loads(request.body)
		user = User.objects.get(pk=data['userid'])
		sesion = Session.objects.get(pk=data['sessionid'])
		s = sesion.get_decoded()
		if (user is not None) and (data['userid'] == s['_auth_user_id']):
			request.user = user
			logout(request)
			sesion.delete()
			context = {'logout':True}
			return self.render_to_json_response(context)
		else:
			return HttpResponseForbidden()

		


@method_decorator(csrf_exempt, name='dispatch')
class UserLogin(JsonResponseMixin, View):

	template_name = 'hamster/login.html'
	form_class = frm.FormLogin
	model_class = User


	def post(self, request, *args, **kwargs):

		data = json.loads(request.body)
		form = self.form_class(data)

		if form.is_valid():
			credentials = form.cleaned_data
			user = authenticate(username=credentials['username'], password=credentials['password'])
			if user is not None:
				login(request, user)
				session_key = request.session.session_key
				user_dict = model_to_dict(user, fields=['id', 'username', 'first_name', 'last_name', 'email'])
				context = {'usuario':user_dict}
				context['sessionid'] = session_key
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



@method_decorator(ensure_csrf_cookie, name='dispatch')
class HomePageView(TemplateView):
	template_name = 'hamster/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['saludo'] = 'Hola Hamster'
		return context







		


		
