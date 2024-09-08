from django.contrib import admin
from django.urls import path
from Busca_App import views  # Import the views from your app

urlpatterns = [
    path('', views.form_search_view, name='form_search_view'),
]
