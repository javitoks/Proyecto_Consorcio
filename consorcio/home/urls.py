from django import views
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logueo, name='logueo'),
    path('loguearse/', views.loguearse, name='loguearse'),

]
