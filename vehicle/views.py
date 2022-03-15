from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('afterlogin')
    return render(request, 'vehicle/index.html')

def is_staff(user):
    return user.groups.filter(name='STAFF').exists()

def afterlogin(request):
    if is_staff(request.user):
        return redirect('staff/staffdashboard')
    else:
        return redirect('admin-dashboard')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict= {
        'staff':model.staff.objects.get(user=request.user)
    }
    return render(request, 'vehicle/admin_dashboard.html', context=dict)

@login_required(login_url='adminlogin')
def adminlogin_view(request):
    staffs=model.staff.objects.all()
    return render(request, 'vehicle/admin_view_staffs.html', {'staffs':staffs})