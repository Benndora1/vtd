
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth.views import LogoutView,LoginView
from vehicle import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),
    
    path('', views.home_view, name='home'),
    path('logout/', LogoutView.as_view(template_name='vehicles/logout.html'), name='logout'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    
    path('adminlogin/', views.adminlogin_view, name='adminlogin'),
]
