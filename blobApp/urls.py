from django.urls import path, re_path
from blobApp import views

urlpatterns = [
    path('b/', views.blobApi ),
    re_path(r'^b\/([a-zA-Z0-9_-]+)$', views.blobApi ),
]