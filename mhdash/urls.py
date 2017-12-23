from django.conf.urls import url, include
from django.contrib import admin
from . import views

from mhdash.models import Carouseldata

from django.views.generic import ListView
from django.views.generic import DetailView

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Carouseldata.objects.all(), template_name="mhdash/index.html")),
    url(r'^$', views.index),
]
