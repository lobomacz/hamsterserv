from django.contrib.admin import AdminSite, ModelAdmin, TabularInline, StackedInline
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis.admin import OSMGeoAdmin
from django.core.exceptions import PermissionDenied, ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from suir.models import *
import datetime

# Register your models here.

class SuirAdmin(AdminSite):

	site_header = 'Administración SUIR'
	site_title = 'Admin SUIR'
	index_title = site_title
	site_url = '/'


class CarruselAdmin(ModelAdmin):

	list_display = ['titulo', 'activo']
	exclude = ['deleted_at', 'updated_at']



class AnuncioAdmin(ModelAdmin):

	list_display = ['titulo', 'activo']


class IndicadorAdmin(ModelAdmin):

	ordering = ['titulo', 'activo', 'seguimiento']
	readonly_fields = ['creador']
	empty_value_display = '-Vacío-'
	search_fields = ['titulo']
	autocomplete_fields = ['sector', 'tipo_valor', 'periodicidad', 'entidad', 'desagregaciones', 'estado']
	filter_horizontal = ['colaboradores']

	def has_change_permission(self, request, obj=None):

		if request.user.is_superuser:

			return True

		if obj == None and not request.user.has_perm('suir.add_indicador'):

			return False

		elif obj != None and request.user == obj.creador or request.user.groups.filter(name__in=['Director', 'Supervisor']).exists():
			
			return True

		else:

			return False


	def save_model(self, request, obj, form, change):
		
		if not change:
			obj.creador = request.user

		super().save_model(request, obj, form, change)



class ValorAdmin(ModelAdmin):

	ordering = ['indicador', '-fecha', 'estado']
	exclude = ['digitador', 'supervisor']
	date_hierarchy = 'fecha'
	empty_value_display = '-NA-'
	list_display = ('fecha', 'indicador','valor')
	autocomplete_fields = ['indicador', 'entidad', 'etnia', 'estado']


	def has_change_permission(self, request, obj=None):

		if request.user.is_superuser:

			return True

		if obj == None and not request.user.has_perm('suir.add_valorindicador'):

			return False

		elif request.user == obj.digitador or  request.user.groups.filter(name='Supervisor').exists():
			
			return True

		else:

			return False



	def formfield_for_foreignkey(self, db_field, request, **kwargs):

		if db_field.name == 'etnia':
			
			kwargs['queryset'] = DetalleTabla.objects.filter(tabla__tabla='etnias')

		elif db_field.name == 'estado':

			kwargs['queryset'] = DetalleTabla.objects.filter(tabla__tabla='estados_pub')

		elif db_field.name == 'rango_edad':

			kwargs['queryset'] = DetalleTabla.objects.filter(tabla__tabla='rangos_edad')

		return super().formfield_for_foreignkey(db_field, request, **kwargs)


	
	def save_model(self, request, obj, form, change):

		if not change:
			obj.digitador = request.user
		else:
			if obj.estado.elemento == 'publicado' and obj.supervisor == None:
				if not request.user.groups.filter(name='Supervisor').exists():
					raise PermissionDenied("No tiene permisos de publicar valores de indicador.")
				else:
					obj.supervisor = request.user

		super().save_model(request, obj, form, change)



class DetalleTablaInline(TabularInline):
	model = DetalleTabla
	ordering = ['elemento']


class TablaAdmin(ModelAdmin):
	inlines = [
		DetalleTablaInline,
	]


class DetalleTablaAdmin(ModelAdmin):

	search_fields = ['elemento']
	ordering = ['tabla', 'elemento']



class PublicacionAdmin(ModelAdmin):

	ordering = ['fecha', 'estado', 'autor', 'titulo']
	exclude = ['autor', 'deleted_at']
	readonly_fields = ('publicado',)
	date_hierarchy = 'fecha'
	empty_value_display = '-NA-'
	list_display = ('slug','titulo')
	formfield_overrides = {
		RichTextUploadingField: {'widget':CKEditorUploadingWidget}
	}
	
	prepopulated_fields = {'slug':('titulo',)}

	class Media:
		css = {
			'all': ('suir/css/admin.css',)
		}


	def has_change_permission(self, request, obj=None):

		if request.user.is_superuser:
			
			return True

		if obj == None:

			return True

		else:

			if request.user == obj.autor:

				return True

			elif obj.tipo.elemento == 'noticia' and request.user.groups.filter(name='Publicador').exists():

				return True

			elif obj.tipo.elemento == 'informe' and request.user.groups.filter(name='Supervisor').exists():

				return True

			else:

				return False


	def get_queryset(self, request):

		queryset = super().get_queryset(request)

		if request.user.is_superuser or request.user.groups.filter(name='Director').exists():
			
			return queryset

		elif request.user.groups.filter(name='Publicador').exists():

			return queryset.filter(tipo__elemento='noticia')

		elif request.user.groups.filter(name='Supervisor').exists():

			return queryset.filter(tipo__elemento='informe')

		return queryset.filter(autor=request.user)


	def save_model(self, request, obj, form, change):

		if not change:
			print(obj.tipo)

			if obj.tipo.elemento == 'noticia':

				if not request.user.has_perms(['suir.crear_noticia', 'suir.add_publicacion']):
					print('Sin permisos de crear')
					
					raise PermissionDenied("No tiene permiso para crear noticias.")

			else:

				if not request.user.has_perms(['suir.crear_informe', 'suir.add_publicacion']):

					raise PermissionDenied("No tiene permiso para crear informes.")

			obj.autor = request.user
			

		if not obj.autor == request.user:

			if obj.tipo.elemento == 'noticia':


				if not request.user.has_perms(['suir.crear_noticia','suir.publicar_noticia', 'suir.change_publicacion']):
					
					raise PermissionDenied("No tiene permiso para crear/publicar noticias.")

			else:

				if not request.user.has_perms(['suir.crear_informe', 'suir.publicar_informe', 'suir.change_publicacion']):

					raise PermissionDenied("No tiene permiso para crear/publicar informes.")


		if obj.estado.elemento == 'publicado' and obj.publicado == None:
			obj.publicado = datetime.datetime.now()

		super().save_model(request, obj, form, change)



	def formfield_for_foreignkey(self, db_field, request, **kwargs):

		if db_field.name == 'tipo':

			if request.user.groups.filter(name='Periodista').exists():

				kwargs["queryset"] = DetalleTabla.objects.filter(elemento='noticia')

			elif request.user.groups.filter(name='Digitador').exists():

				kwargs["queryset"] = DetalleTabla.objects.filter(elemento='informe')

			else:

				kwargs["queryset"] = DetalleTabla.objects.filter(tabla__tabla='tipos_pub')


		elif db_field.name == 'estado':

			if request.user.groups.filter(name__in=['Periodista', 'Digitador']).exists():

				kwargs["queryset"] = DetalleTabla.objects.filter(elemento='borrador')

			else:

				kwargs["queryset"] = DetalleTabla.objects.filter(tabla__tabla='estados_pub')


		return super().formfield_for_foreignkey(db_field, request, **kwargs)



class EntidadAdmin(ModelAdmin):

	ordering = ['sector', 'nombre']
	autocomplete_fields = ['sector']
	search_fields = ['nombre']


class MunicipioAdmin(OSMGeoAdmin):

	ordering = ['nombre']
	search_fields = ['nombre', 'nombre_corto']


class ComunidadAdmin(OSMGeoAdmin):

	ordering = ['municipio', 'nombre']
	list_display = ['municipio', 'nombre']
	search_fields = ['municipio', 'nombre', 'actividades_ec']


class SuirUserAdmin(UserAdmin):
	model = User


class TransmisionAdmin(ModelAdmin):

	exclude = ['publicador', 'created_at', 'updated_at']
	ordering = ['created_at', 'inicio']
	list_display = ['descripcion', 'publicador', 'especial', 'created_at']


	def save_model(self, request, obj, form, change):
		
		if not change:

			obj.publicador = request.user

		super().save_model(request,obj,form,change)


	def has_change_permission(self, request, obj=None):

		if request.user.is_superuser or obj == None:
			return True

		if request.user.has_perm('suir.change_transmision') or request.user == obj.publicador:
			return True
		else:
			return False
