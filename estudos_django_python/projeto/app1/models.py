from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Cliente(models.Model):
	id_cliente = models.CharField(max_length=200)
	nome_cliente = models.CharField(max_length=200)
	sexo = models.CharField(max_length=1)
	tipo = models.CharField(max_length=1)
	dia_pagamento = models.IntegerField()

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	salary = models.DecimalField(max_digits=5, decimal_places=2)
	bio = models.TextField()
	#photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
	
	def __str__(self):
		return self.first_name+' '+self.last_name