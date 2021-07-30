from django.contrib.admin import AdminSite
from hamster.models import *

# Register your models here.

class HamsterAdmin(AdminSite):

	site_header = 'Administración Hamster App'
	site_title = 'Hamster Admin'
	index_title = site_title
	site_url = '/hamster'

hamster_admin = HamsterAdmin(name='hamsteradmin')

hamster_admin.register(Institucion)
hamster_admin.register(Funcionario)
hamster_admin.register(Beneficiario)
hamster_admin.register(Contribucion)