from django import views
from django.contrib import admin
from django.urls import path
from casa import views


urlpatterns = [
    path('casas/', views.listado_casas, name='listado_casas'),
    path('propietarios/', views.listado_propietarios, name='propietarios'),
    path('inquilinos/', views.listado_inquilinos, name='inquilinos')
]