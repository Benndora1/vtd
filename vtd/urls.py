from django.contrib import admin
from django.urls import path , include
from vehicle import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),
    
    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='vehicle/logout.html'), name='logout'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    
    path('adminlogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-staff/', views.admin_view_staff_view, name='admin-view-staff'),
    path('update-staffs/<int:pk>', views.update_staffs_view, name='update-staffs'),
    path('delete-staffs/<int:pk>', views.delete_staffs_view, name='delete-staffs'),
    
    path('admin-view-vehicles', views.admin_view_vehicles_view, name='admin-view-vehicles'),
    path('update-vehicle/<int:pk>/', views.update_vehicle_view, name='admin-update-vehicles'),
    path('delete-vehicle/<int:pk>/', views.delete_vehicle_view, name='admin-delete-vehicles'),

    path('admin_view_vehicle_holder/', views.admin_view_vehicle_holder_view, name='admin_view_vehicle_holder'),
    path('admin_view_approved_vehicle_holder/', views.admin_view_approved_vehicle_holder_view, name='admin_view_approved_vehicle_holder'),
    path('admin_view_disapproved_vehicle_holder/', views.admin_view_diasspproved_vehicle_holder_view, name='diasspproved_vehicle_holder'),
    path('admin_view_waiting_vehicle_holder', views.admin_view_waiting_vehicle_holder_view, name='admin_view_waiting_vehicle_holder'),


]
