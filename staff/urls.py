from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('staffclick/', views.staffclick_view, name='staffclick'),
    path('staffsignup/', views.staffsignup_view, name='staffsignup'),
    path('stafflogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='stafflogin'),
    path('staffdashboard/', views.staff_dashboard_view, name='staffdashboard'),
]