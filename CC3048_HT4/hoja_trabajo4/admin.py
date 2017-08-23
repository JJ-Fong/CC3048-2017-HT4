# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Receta)

# Register your models here.
