from django.forms import ModelForm
from .models import Clientes

class PersonForm(ModelForm):
	class Meta:
		model = Clientes
		fields = ['id_cliente','nome_cliente' ,'sexo','tipo','dia_pagamento']


