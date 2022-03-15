from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

urlpatterns = [
    path('staffclick/', views.staffclick_view, name='staffclick'),
    path('staffsignup/', views.staffsignup_view, name='staffsignup'),
    path('stafflogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='stafflogin'),
    path('staffdashboard/', views.staff_dashboard_view, name='staffdashboard'),
  

    path(('request_vehicle/'), views.request_vehicle_view, name='request_vehicle'),
    path('request_vehicle/<int:pk>/', views.request_vehicle_view, name='request_vehicle'),
    # path('history/', views.history_view, name='history'),
]