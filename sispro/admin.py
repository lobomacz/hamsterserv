from django.contrib.admin.sites import AdminSite
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.urls import reverse
from sispro.models import *

# Register your models here.

class SisproAdminSite(AdminSite):
	site_header = 'Admin SISPRO'
	site_title = site_header
	site_url = '/sispro/'
	index_title = site_title


class ProyectoInline(StackedInline):
	model = Proyecto
	ordering = ['programa', 'codigo']


class ProgramaAdmin(ModelAdmin):
	model = Programa
	ordering = ['codigo']
	inlines = [
		ProyectoInline,
	]

class ProtagonistaAdmin(ModelAdmin):
	model = Protagonista
	ordering = ['comunidad__municipio__nombre', 'comunidad__nombre', 'apellidos']


class TecnicoAdmin(ModelAdmin):
	model = Tecnico
	ordering = ['comunidad__municipio__nombre', 'comunidad__nombre', 'apellidos']




