from django import forms 
from hamster.models import Contribucion, Beneficiario 

class FormContribucion(forms.ModelForm):
	"""
	Formulario del modelo Contribucion
	"""
	class Meta:
		model = Contribucion


class FormBeneficiario(forms.ModelForm):
	"""docstring for FormBeneficiario"""
	def __init__(self, arg):
		super(FormBeneficiario, self).__init__()
		self.arg = arg
		
