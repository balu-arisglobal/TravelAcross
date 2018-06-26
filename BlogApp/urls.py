from django.urls import path
from django.conf.urls import url
from BlogApp import views

urlpatterns = [
    path('', views.index),
]