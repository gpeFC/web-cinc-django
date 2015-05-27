"""webCInC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from cinc.views import inicio, cinc, investigacion, investigadores, lineas_investigacion, publicaciones, administracion, actas, oferta_educativa, departamentos, contacto

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio),
    url(r'^inicio/$', inicio),
    url(r'^cinc/$', cinc),
    url(r'^investigacion/$', investigacion),
    url(r'^investigadores/$', investigadores),
    url(r'^lineas-investigacion/$', lineas_investigacion),
    url(r'^publicaciones/$', publicaciones),
    url(r'^administracion/$', administracion),
    url(r'^actas/$', actas),
    url(r'^oferta-educativa/$', oferta_educativa),
    url(r'^departamentos/$', departamentos),
    url(r'^contacto/$', contacto),
    url(r'^cargas/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
]
