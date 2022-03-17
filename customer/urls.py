from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

urlpatterns = [
    
    path('customerclick/', views.customerclick_view, name='customerclick'),
    path('customerlogin/', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='customerlogin'),
    path('customersignup/', views.customer_signup_view, name='customersignup'),
    path('customerdashboard', views.customer_dashboard_view, name='customerdashboard'),
    path(('request-vehicle/'), views.request_vehicle_view, name='request-vehicle'),
    path('request_vehicle/<int:pk>/', views.request_vehicle_view, name='request_vehicle'),
    path('history/', views.history_view, name='history'),
]