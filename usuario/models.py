# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class usuario(models.Model):
	user = models.CharField(max_length=15)
	pwd = models.CharField(max_length=20)

class restaurante(models.Model):
	foto = models.ImageField(upload_to='../static')
	nombre = models.CharField(max_length=20)
	valoracion = models.CharField(max_length=5)
	ciudad = models.CharField(max_length=15)