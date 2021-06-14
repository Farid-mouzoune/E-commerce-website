from django.contrib import admin
from django.urls import path, include
from .views import homepath


urlpatterns = [
    path('', homepath, name='home'),


]