from django.db import models
from django.contrib import admin

# Create your models here.
from django.db import models

class Clientes(models.Model):
	id_cliente = models.CharField(max_length=200, primary_key = True)
	nome_cliente = models.CharField(max_length=200)
	sexo = models.CharField(max_length=1)
	tipo = models.CharField(max_length=1)
	dia_pagamento = models.IntegerField()

	class Meta:
		db_table = 'clientes'

class Servicos(models.Model):
	id_servicos = models.CharField(max_length=200, primary_key = True)
	nome_servico = models.CharField(max_length=200)
	preco_servico = models.DecimalField(max_digits = 5 , decimal_places = 5)
	data_cadastro_dt = models.DateField()

	class Meta:
		db_table = 'servicos'

class Cliente_servicos(models.Model):
	id_cli_serv = models.CharField(max_length=200, primary_key = True)
	id_servico = models.CharField(max_length=200)
	id_cliente = models.CharField(max_length=200)
	inicio_contrato = models.DateField()
	fim_contrato = models.DateField()

	class Meta:
		db_table = 'cliente_servicos'