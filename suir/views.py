from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from suir.models import Anuncio, Carrusel, Indicador, Tabla, Publicacion, LinkExterno, LinkRed
import datetime
# from suir.serializers import *
# from suir.permissions import ReadOnlyAllowed
# from rest_framework import generics, status, viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response 
# from rest_framework.decorators import action
# import json


# Create your views here.

PAGINAS = settings.SUIR_CONF['paginas']

class InicioView(TemplateView):

	template_name = 'suir/inicio.html'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)

		carrusel = Carrusel.objects.filter(activo=True)
		promovidos = Publicacion.objects.filter(carrusel=True)
		anuncios = Anuncio.objects.filter(activo=True)
		noticias = Publicacion.objects.filter(tipo__elemento='noticia', estado__elemento='publicado')[:4]
		informes = Publicacion.objects.filter(tipo__elemento='informe', estado__elemento='publicado')[:4]
		enlaces = LinkExterno.objects.filter(activo=True)
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
		context = super().get_context_data(kwargs)

		enlaces = LinkExterno.objects.filter(activo=True)
		redes = LinkRed.objects.filter(activo=True)

		context['enlaces'] = enlaces
		context['redes'] = redes 

		context['fecha'] = datetime.datetime.now()

		return context


class SuirDetailView(DetailView):

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)

		enlaces = LinkExterno.objects.filter(activo=True)
		redes = LinkRed.objects.filter(activo=True)

		context['enlaces'] = enlaces
		context['redes'] = redes 

		context['fecha'] = datetime.datetime.now()

		return context



class ListaNoticiasView(SuirListView):
	paginate_by = PAGINAS
	template_name = 'suir/grid_list.html'
	queryset = Publicacion.objects.filter(tipo__elemento='noticia')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		paginador = context['paginator']
		page_obj = context['page_obj']
		elided_range = paginador.get_elided_page_range(page_obj.number, on_each_side=3, on_ends=3)
		context['elided_range'] = elided_range
		context['tipo'] = 'noticia'
	
		return context


class DetalleNoticiaView(SuirDetailView):
	model = Publicacion
	context_object_name = 'publicacion'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		context['tipo'] = 'noticia'
		context['tags'] = [tag.strip() for tag in  self.get_object().tags.split(',')]
		
		return context 
	

class ListaInformesView(SuirListView):
	paginate_by = PAGINAS
	template_name = 'suir/grid_list.html'
	queryset = Publicacion.objects.filter(tipo__elemento='informe')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		paginador = context['paginator']
		page_obj = context['page_obj']
		elided_range = paginador.get_elided_page_range(page_obj.number, on_each_side=3, on_ends=3)
		context['elided_range'] = elided_range
		context['tipo'] = 'informe'

		return context


class DetalleInformeView(SuirDetailView):
	model = Publicacion
	context_object_name = 'publicacion'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		context['tipo'] = 'informe'
		context['fecha'] = datetime.datetime.now()
		return context 


class ListaIndicadoresView(SuirListView):
	paginate_by = 15
	model = Indicador

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		context['tipo'] = 'indicador'

		return context


class DetalleIndicadorView(SuirDetailView):
	model = Indicador
	context_object_name = 'indicador'



""" 
class AnuncioViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Anuncio.objects.all()
	serializer_class = sAnuncio
	permission_classes = [ReadOnlyAllowed]

	@action(detail=False)
	def activos(self, request):
		anuncios = self.get_queryset().filter(activo=True)
		serializer = self.get_serializer(anuncios, many=True)
		return Response(serializer.data)
		


class TablaViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Tabla.objects.all()
	serializer_class = sTabla
	permission_classes = [ReadOnlyAllowed]

	@action(detail=False)
	def filtro(self, request):
		nombre = request.query_params.get('nombre')
		tabla = self.get_queryset().filter(tabla=nombre)
		serializer = self.get_serializer(tabla, many=False)
		return Response(serializer.data)


class IndicadorViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Indicador.objects.all()
	serializer_class = sIndicador 
	permission_classes = [ReadOnlyAllowed]

	@action(detail=False)
	def publicados(self, request):
		indicadores = self.get_queryset().filter(estado__elemento="publicado")
		serializer = self.get_serializer(indicadores, many=True)
		return Response(serializer.data)



class LinkExternoViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = LinkExterno.objects.all()
	serializer_class = sLinkExterno
	permission_classes = [ReadOnlyAllowed]

	@action(detail=False)
	def activos(self, request):
		enlaces = self.get_queryset().filter(activo=True)
		serializer = self.get_serializer(enlaces, many=True)
		return Response(serializer.data)



class PublicacionViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Publicacion.objects.all()
	serializer_class = sPublicacion
	permission_classes = [ReadOnlyAllowed]

	@action(detail=False, serializer_class=sThumbPublicacion)
	def carrusel(self, request):
		publicaciones = self.get_queryset().filter(carrusel=True, estado__elemento="publicado")
		serializer = self.get_serializer(publicaciones, many=True)
		return Response(serializer.data)


	@action(detail=False, serializer_class=sThumbPublicacion)
	def lista_noticias(self, request):
		noticias = self.get_queryset().filter(estado__elemento="publicado", tipo__elemento="noticia")
		serializer = self.get_serializer(noticias, many=True)
		return Response(serializer.data)


	@action(detail=False, serializer_class=sThumbPublicacion)
	def lista_informes(self, request):
		informes = self.get_queryset().filter(estado__elemento="publicado", tipo__elemento="informe")
		serializer = self.get_serializer(informes, many=True)
		return Response(serializer.data)


""" 
