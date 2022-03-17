from django.contrib import admin
from django.urls import path , include
from vehicle import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),

    path('customer/', include('customer.urls')),
    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='vehicle/logout.html'), name='logout'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    
    path('adminlogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer/', views.admin_view_customer_view, name='admin-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view, name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view, name='delete-customer'),
    
    path('admin-view-vehicles', views.admin_view_vehicles_view, name='admin-view-vehicles'),
    path('update-vehicle/<int:pk>/', views.update_vehicle_view, name='admin-update-vehicles'),
    path('delete-vehicle/<int:pk>/', views.delete_vehicle_view, name='admin-delete-vehicles'),

    path('admin-add-vehicle', views.admin_add_vehicle_view, name='admin-add-vehicle'),
    path('admin-view-vehicle', views.admin_view_vehicles_view, name='admin-view-vehicle'),




    path('admin_view_vehicle_holder/', views.admin_view_vehicle_holder_view, name='admin_view_vehicle_holder'),
    path('admin_view_approved_vehicle_holder/', views.admin_view_approved_vehicle_holder_view, name='admin_view_approved_vehicle_holder'),
    path('admin_view_disapproved_vehicle_holder/', views.admin_view_diasspproved_vehicle_holder_view, name='diasspproved_vehicle_holder'),
    path('admin_view_waiting_vehicle_holder', views.admin_view_waiting_vehicle_holder_view, name='admin_view_waiting_vehicle_holder'),


]
