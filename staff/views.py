from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
from datetime import date, timedelta
from django.contrib.auth.models import Group
from vehicle import models as CMODEL
from vehicle import forms as CFORM



def staffclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'staff/staffclick.html')


def staff_signup_view(request):
    userForm=forms.StaffUserForm()
    staffForm=forms.StaffForm()
    mydict={'userForm':userForm, 'staffForm':staffForm}
    if request.method=='POST':
        userForm=forms.StaffUserForm(request.POST)
        staffForm=forms.StaffForm(request.POST)
        if userForm.is_valid() and staffForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            staff=staffForm.save(commit=False)
            staff.user=user
            staff.save()
            my_staff_group = Group.objects.get_or_create(name='staff')
            my_staff_group[0].user_set.add(user)
        return HttpResponseRedirect('stafflogin')
    return render(request, 'staff/staffsignup.html', context=mydict)

def is_staff(user):
    return user.groups.filter(name='STAFF').exists()


@login_required(login_url='stafflogin')
def staff_dashboard_view(request):
    dict= {
        'staff':model.staff.objects.get(user=request.user)
        'available_vehicles':models.Vehicle.objects.all().count()
        'total_vehicle_holders':models.VehicleRecord.objects.all().count(),
    }
 
    return render(request, 'staff/staffdashboard.html', context=dict)

def request_vehicle_view(request):
    staff = models.Staff.objects.get(user_id=request.user.id)
    vehicles = CMODEL.vehicles.objects.all()
    return render(request, 'staff/request_vehicle.html', {'staff': staff, 'vehicles': vehicles})

def requested_vehicles_view(request):
    staff = models.Staff.objects.get(user_id=request.user.id)
    vehicles = CMODEL.Vehicles.objects.get(id=pk)
    vehiclerecords = CMODEL.VehicleRecord()
    vehiclerecords.vehicle = vehicle
    vehiclerecords.staff = staff
    vehiclerecords.save()
    return redirect('history')

def histroy_view(request):
    staff = models.Staff.objects.get(user_id=request.user.id)
    vehicle = CMODEL.VehicleRecord.objects.all.filter(staff=staff)
    return render(request, 'staff/history.html', {'staff': staff, 'vehicles': vehicles})