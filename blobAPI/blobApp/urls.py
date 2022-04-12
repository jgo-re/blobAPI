import imp
from django.urls import path
from django.conf.urls import url
from blobApp import views

urlpatterns = [
    path('b/', views.blobApi ),
    url(r'^b\/([a-zA-Z0-9_-]+)$', views.blobApi ),
]