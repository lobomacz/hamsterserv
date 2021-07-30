from django.contrib.admin import AdminSite, ModelAdmin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from suir.models import *
import datetime

# Register your models here.

class SuirAdmin(AdminSite):

	site_header = 'Administración SUIR'
	site_title = 'Admin SUIR'
	index_title = site_title
	site_url = '/suir'



class IndicadorAdmin(ModelAdmin):

	ordering = ['titulo', 'activo', 'seguimiento']
	readonly_fields = ['creador']
	empty_value_display = '-Vacío-'
	search_fields = ['titulo']
	autocomplete_fields = ['sector', 'tipo_valor', 'periodicidad', 'entidad', 'desagregacion', 'estado']
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
	autocomplete_fields = ['indicador', 'entidad', 'nivel', 'etnia', 'estado']

	
	def save_model(self, request, obj, form, change):

		if not change:
			obj.digitador = request.user
		else:
			if obj.estado.elemento == 'publicado' and obj.supervisor == None:
				obj.supervisor = request.user

		super().save_model(request, obj, form, change)



class DetalleTablaAdmin(ModelAdmin):

	search_fields = ['elemento']
	ordering = ['tabla', 'elemento']



class PublicacionAdmin(ModelAdmin):

	ordering = ['fecha', 'estado', 'autor', 'titulo']
	exclude = ['autor']
	readonly_fields = ('publicado', 'slug')
	date_hierarchy = 'fecha'
	empty_value_display = '-Vacío-'
	formfield_overrides = {
		RichTextUploadingField: {'widget':CKEditorWidget}
	}
	autocomplete_fields = ['tipo', 'estado']
	prepopulated_fields = {'slug':('titulo',)}

	def save_model(self, request, obj, form, change):

		if not change:
			obj.autor = request.user

		if obj.estado.elemento == 'publicado' and obj.publicado == None:
			obj.publicado = datetime.datetime.now()

		super().save_model(request, obj, form, change)


class EntidadAdmin(ModelAdmin):

	ordering = ['sector', 'nombre']
	autocomplete_fields = ['sector']
	search_fields = ['nombre']




suir_admin = SuirAdmin(name='suiradmin')

suir_admin.register(Anuncio)
suir_admin.register(Contacto)
suir_admin.register(Tabla)
suir_admin.register(DetalleTabla, DetalleTablaAdmin)
suir_admin.register(Entidad, EntidadAdmin)
suir_admin.register(Indicador, IndicadorAdmin)
suir_admin.register(ValorIndicador, ValorAdmin)
suir_admin.register(Institucion)
suir_admin.register(LinkExterno)
suir_admin.register(Publicacion, PublicacionAdmin)
