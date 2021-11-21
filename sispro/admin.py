from django.contrib.admin.sites import AdminSite
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.urls import reverse
from sispro.models import *

# Register your models here.

class SisproAdminSite(AdminSite):
	site_header = 'Admin SISPRO'
	site_title = site_header
	site_url = reverse('index_sispro')
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





