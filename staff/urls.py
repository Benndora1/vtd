from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('staffsignup/', views.staffsignup_view, name='staffsignup'),
]