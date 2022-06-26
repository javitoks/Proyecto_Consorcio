from django import views
from django.contrib import admin
from django.urls import path
from casa import views


urlpatterns = [
    path('', views.listado_casas, name='listado_casas')
]