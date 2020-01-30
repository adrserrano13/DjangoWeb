from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from usuario import models


def inicio (request):
   	
	if 'nombre' in request.GET:
		user = request.GET['nombre']
		contrasena = request.GET['contrasena']

		comprobar = models.usuario.objects.filter(user = user)

		if comprobar:
			lista_usuario = models.usuario.objects.get(user = user)

			if user == lista_usuario.user and contrasena == lista_usuario.pwd:
				x = False
				return render(request,"pagina.html",{'x': x,'usuario': user})
				
			else:
				x = True
				return render(request,"pagina.html",{'x': x,'usuario': user})

		else:
			x = True
			return render(request,"pagina.html",{'x': x,'usuario': user})
	
	else:
		x = True
		return render(request,"pagina.html",{'x': x})


def restaurante (request):

	url = models.restaurante.objects.filter(ciudad = request.GET['ciu'])

    	return render(request, 'restaurante.html' ,{'foto' : url})


def registro(request):

	if 'user' in request.GET:
			
			user = request.GET['user']
			pwd = request.GET['pwd']

			usuario = models.usuario(user = user,pwd = pwd)
			usuario.save()


			return render(request,"registro.html",{})

	else:
		return render(request,"registro.html",{})





           