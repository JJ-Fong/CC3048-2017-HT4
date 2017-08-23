# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 20)
 	precio = models.FloatField(null = False, blank = False)
	
class Ingrediente(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 20)
	costo = models.FloatField(null = False, blank = False)

class Receta(models.Model):
	id_prod = models.ForeignKey(Producto, on_delete = models.CASCADE)
	id_ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
	