from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('web_hook', views.web_hook, name='web_hook'),
]