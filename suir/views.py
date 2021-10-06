from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import View 
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from suir.models import Anuncio, Carrusel, Indicador, Tabla, Publicacion, LinkExterno, LinkRed
from suir.forms import *
import datetime


# Create your views here.

PAGINAS = settings.SUIR_CONF['paginas']

class InicioView(TemplateView):

	template_name = 'suir/inicio.html'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)

		carrusel = Carrusel.objects.filter(activo=True)
		promovidos = Publicacion.objects.filter(carrusel=True).order_by('-fecha')[:5]
		anuncios = Anuncio.objects.filter(activo=True)
		noticias = Publicacion.objects.filter(tipo__elemento='noticia', estado__elemento='publicado')[:4]
		informes = Publicacion.objects.filter(tipo__elemento='informe', estado__elemento='publicado')[:4]
		enlaces = LinkExterno.objects.filter(activo=True)[:6]
		redes = LinkRed.objects.filter(activo=True)
		

		context['carrusel'] = carrusel
		context['promovidos'] = promovidos
		context['anuncios'] = anuncios
		context['noticias'] = noticias
		context['informes'] = informes
		context['enlaces'] = enlaces
		context['redes'] = redes 
		context['carrusel_count'] = len(carrusel) + len(promovidos)
		context['fecha'] = datetime.datetime.now()

		return context


class SuirListView(ListView):

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		paginator = context['paginator']

		enlaces = LinkExterno.objects.filter(activo=True)[:6]
		redes = LinkRed.objects.filter(activo=True)

		context['enlaces'] = enlaces
		context['redes'] = redes 

		context['fecha'] = datetime.datetime.now()

		context['rango_paginas'] = paginator.get_elided_page_range(self.request.GET.get('page',1), on_each_side=3, on_ends=3)

		return context


class SuirDetailView(DetailView):

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		enlaces = LinkExterno.objects.filter(activo=True)[:6]
		redes = LinkRed.objects.filter(activo=True)

		context['enlaces'] = enlaces
		context['redes'] = redes 

		context['fecha'] = datetime.datetime.now()

		return context


class SuirCreateEditMixin(LoginRequiredMixin, PermissionRequiredMixin):

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		enlaces = LinkExterno.objects.filter(activo=True)[:6]
		redes = LinkRed.objects.filter(activo=True)

		context['enlaces'] = enlaces
		context['redes'] = redes 

		context['fecha'] = datetime.datetime.now()

		return context



# class LoginView(FormView):
# 	"""
# 	Vista de ingreso de usuarios
# 	"""
# 	template_name = 'suir/login.html'
# 	form_class = LoginForm
# 	success_url = reverse_lazy('inicio')

# 	def form_valid(self, form):
		
# 		data = form.cleaned_data
# 		nombreusuario = data['username']
# 		contrasena = data['contrasena']

# 		usuario = authenticate(self.request, nombreusuario, contrasena)

# 		if usuario is not None:
# 			login(self.request, usuario)
# 			return super().form_valid(form)
# 		else:
# 			return super().form_invalid(form)


# class LogoutView(View):

# 	def get(self, request, *args, **kwargs):
# 		logout(request)
# 		return redirect('inicio')



class ListaPublicacionesView(SuirListView):
	paginate_by = PAGINAS
	template_name = 'suir/grid_list.html'
	tipo = ''

	def get_queryset(self):
		return Publicacion.objects.filter(tipo__elemento=self.tipo)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = self.tipo
	
		return context


class ListaFiltroPublicacionesView(ListaPublicacionesView):

	def get_queryset(self):
		clave = self.request.GET.get('q').strip()

		return Publicacion.objects.filter(Q(titulo__contains=clave) | Q(tags__contains=clave),tipo__elemento=self.tipo)


class DetallePublicacionView(SuirDetailView):
	model = Publicacion
	context_object_name = 'publicacion'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = self.object.tipo.elemento
		context['tags'] = [tag.strip() for tag in  self.get_object().tags.split(',')]
		
		return context 



class CreatePublicacionView(SuirCreateEditMixin, CreateView):

	model = Publicacion
	form_class = PublicacionForm
	initial = {'fecha':datetime.datetime.now()}
	permission_required = 'suir.add_publicacion'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = self.kwargs.get('tipo')
		return context

	def form_valid(self, form):

		tipo = self.kwargs['tipo']

		if tipo == 'noticia':
			if not self.request.user.has_perm('suir.crear_noticia'):
				raise PermissionDenied("El usuario no tiene permiso para redactar noticias.")
		else:
			if not self.request.user.has_perm('suir.crear_informe'):
				raise PermissionDenied("El usuario no tiene permiso para redactar informes.")

		form.instance.autor = self.request.user
		form.instance.slug = slugify(form.instance.titulo)
		form.instance.tipo = DetalleTabla.objects.filter(elemento=tipo)

		return super().form_valid(form)

	def get_success_url(self):
		tipo = 'detalle_noticia' if self.object.tipo.elemento == 'noticia' else 'detalle_informe'
		return reverse_lazy(tipo, kwargs={'slug':self.object.slug})



class UpdatePublicacionView(SuirCreateEditMixin, UpdateView):

	"""
	Clase para actualización de publicaciones, sólo para el autor de la publicación.
	"""
	model = Publicacion
	form_class = PublicacionForm
	permission_required = 'suir.change_publicacion'

	def form_valid(self, form):

		if form.instance.tipo.elemento == 'noticia':
			if not self.request.user.has_perm('suir.publicar_noticia'):
				raise PermissionDenied("El usuario no tiene permiso para redactar noticias.")
		else:
			if not self.request.user.has_perm('suir.publicar_informe'):
				raise PermissionDenied("El usuario no tiene permiso para redactar informes.")

		if form.instance.autor == self.request.user:
			if form.instance.publicado == None and form.instance.estado == DetalleTabla.objects.filter(elemento='publicado'):
				form.instance.publicado = datetime.datetime.now()
			return super().form_valid(form)
		else:
			raise PermissionDenied("El usuario no es el autor de la publicación.")

	def get_success_url(self):
		tipo = 'detalle_noticia' if self.object.tipo.elemento == 'noticia' else 'detalle_informe'
		return reverse_lazy(tipo, kwargs={'slug':self.object.slug})



class ListaIndicadoresView(SuirListView):
	paginate_by = PAGINAS
	model = Indicador

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = 'indicador'
		return context


class ListaFiltroIndicadoresView(ListaIndicadoresView):

	def get_queryset(self):
		clave = self.request.GET.get('q').strip()
		return Indicador.objects.filter(Q(titulo__contains=clave) | Q(sector__elemento__startswith=clave) | Q(tags__contains=clave))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = 'indicador'
		return context


class DetalleIndicadorView(SuirDetailView):
	model = Indicador
	context_object_name = 'indicador'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tipo'] = 'indicador'
		return context



class ValorIndicadorView(SuirCreateEditMixin, CreateView):

	"""
	Clase para el registro de valores de indicadores.
	"""
	model = ValorIndicador
	form_class = ValorIndicadorForm
	permission_required = 'suir.add_valorindicador'

	def form_valid(self, form):
		
		form.instance.digitador = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		indicador = self.object.indicador 
		return reverse_lazy('detalle_indicador', kwargs={'pk':indicador.pk})



class DetalleValorView(LoginRequiredMixin, SuirDetailView):

	model = ValorIndicador
	context_object_name = 'valor'



class UpdateValorIndicadorView(SuirCreateEditMixin, UpdateView):
	"""
	Clase para actualizar datos o estado de pulicación del valor de indicador.
	"""

	model = ValorIndicador
	form_class = ValorIndicadorForm
	permission_required = 'suir.change_valorindicador'

	def form_valid(self, form):
		
		if form.instance.supervisor != None:
			if form.instance.supervisor != self.request.user:
				raise PermissionDenied("No es el supervisor.")
		else:
			form.instance.supervisor = self.request.user

		return super().form_valid(form)



