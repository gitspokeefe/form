from django.conf.urls import url, include
from django.contrib import admin
from . import views

  # ****************

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^create$', views.create),
    url(r'^entity/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^entity/(?P<id>\d+)/edit$', views.edit),
    url(r'^entity/(?P<id>\d+)/update$', views.update),
    url(r'^logout_view$', views.logout_view),
]
