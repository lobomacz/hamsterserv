from django.contrib.admin import AdminSite, ModelAdmin, TabularInline, StackedInline
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from hamster.models import Funcionario, Beneficiario, Contribucion, Institucion as hInstitucion
from suir.models import *
import datetime

# Register your models here.

#  _   _                             _                      _                    
# | | | |   __ _   _ __ ___    ___  | |_    ___   _ __     / \     _ __    _ __  
# | |_| |  / _` | | '_ ` _ \  / __| | __|  / _ \ | '__|   / _ \   | '_ \  | '_ \ 
# |  _  | | (_| | | | | | | | \__ \ | |_  |  __/ | |     / ___ \  | |_) | | |_) |
# |_| |_|  \__,_| |_| |_| |_| |___/  \__|  \___| |_|    /_/   \_\ | .__/  | .__/ 
#                                                                 |_|     |_|    

# Admin de la aplicación hamster

class HamsterAdmin(AdminSite):

	site_header = 'Administración Hamster App'
	site_title = 'Hamster Admin'
	index_title = site_title
	site_url = None # '/hamster'

hamster_admin = HamsterAdmin(name='hamsteradmin')

hamster_admin.register(hInstitucion)
hamster_admin.register(Funcionario)
hamster_admin.register(Beneficiario)
hamster_admin.register(Contribucion)


#  ____    _   _   ___   ____  
# / ___|  | | | | |_ _| |  _ \ 
# \___ \  | | | |  | |  | |_) |
#  ___) | | |_| |  | |  |  _ < 
# |____/   \___/  |___| |_| \_\
                              

# Admin de la aplicación suir

class SuirAdmin(AdminSite):

	site_header = 'Administración SUIR'
	site_title = 'Admin SUIR'
	index_title = site_title
	#site_url = '/suir'


class IndicadorAdmin(ModelAdmin):

	ordering = ['titulo', 'activo', 'seguimiento']
	readonly_fields = ['creador']
	empty_value_display = '-Vacío-'
	search_fields = ['titulo']
	autocomplete_fields = ['sector', 'tipo_valor', 'periodicidad', 'entidad', 'desagregaciones', 'estado']
	filter_horizontal = ['colaboradores']

	def save_model(self, request, obj, form, change):
		
		if not change:
			obj.creador = request.user

		super().save_model(request, obj, form, change)


class ValorAdmin(ModelAdmin):

	ordering = ['indicador', 'fecha', 'estado']
	exclude = ['digitador']
	date_hierarchy = 'fecha'
	empty_value_display = '-Vacío-'
	list_display = ('fecha', 'indicador')
	autocomplete_fields = ['indicador', 'entidad', 'etnia', 'estado']

	
	def save_model(self, request, obj, form, change):

		if not change:
			obj.digitador = request.user
		else:
			if obj.estado.elemento == 'publicado' and obj.supervisor == None:
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


	def has_change_permission(self, request, obj=None):

		if request.user.is_superuser:
			
			return True

		if obj == None:

			return True

		else:

			if request.user == obj.autor or request.user.groups.filter(name__in=['Supervisor', 'Director', 'Publicador']).exists():

				return True

			else:

				return False



	def get_queryset(self, request):

		queryset = super().get_queryset(request)

		if request.user.is_superuser:
			return queryset
		return queryset.filter(autor=request.user)


	def save_model(self, request, obj, form, change):

		if obj.tipo == 'noticia':

			if not request.user.has_perms(['suir.crear_noticia','suir.publicar_noticia']):
				
				raise PermissionDenied("No tiene permiso para crear/publicar noticias.")

		else:

			if not request.user.has_perms(['suir.crear_informe', 'suir.publicar_informe']):

				raise PermissionDenied("No tiene permiso para crear/publicar informes.")

		if not change:
			obj.autor = request.user
			
		#else:
		#
		#	if not request.user == obj.autor or not request.user.groups.filter(name__in=['Supervisor', 'Director', 'Publicador']).exists() or not request.user.is_superuser:
		#		
		#		raise PermissionDenied("No tiene permiso para editar este registro.")

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


class ComunidadInline(TabularInline):

	model = Comunidad
	ordering = ['nombre']



class MunicipioAdmin(ModelAdmin):

	ordering = ['nombre']
	search_fields = ['nombre', 'nombre_corto']
	inlines = [
		ComunidadInline,
		]


class ComunidadAdmin(ModelAdmin):

	ordering = ['municipio', 'nombre']
	search_fields = ['municipio', 'nombre', 'actividades_ec']



suir_admin = SuirAdmin(name='suiradmin')

suir_admin.register(Anuncio)
suir_admin.register(Contacto)
suir_admin.register(Tabla, TablaAdmin)
suir_admin.register(DetalleTabla, DetalleTablaAdmin)
suir_admin.register(Entidad, EntidadAdmin)
suir_admin.register(Municipio, MunicipioAdmin)
suir_admin.register(Comunidad, ComunidadAdmin)
suir_admin.register(Indicador, IndicadorAdmin)
suir_admin.register(ValorIndicador, ValorAdmin)
suir_admin.register(Institucion)
suir_admin.register(LinkExterno)
suir_admin.register(LinkRed)
suir_admin.register(Publicacion, PublicacionAdmin)
suir_admin.register(Carrusel)