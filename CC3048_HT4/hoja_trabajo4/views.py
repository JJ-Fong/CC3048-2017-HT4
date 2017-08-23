# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
# Create your views here.
from .models import *

def index(request):
	return render(request, '../templates/index.html')


def orden(request):
	menu = Producto.objects.all()
	context = {'menu': menu}
	print request.POST
	return render(request, '../templates/orden_view.html', context)
