from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'hello-world/', views.index, name='index'),
	url(r'orden/', views.orden, name='index'),
]