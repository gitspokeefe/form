from django.conf.urls import url, include
from django.contrib import admin
from . import views     # This line is new!

urlpatterns = [
    url(r'^', views.index),
    url(r'^processform$', views.my_view),
]
