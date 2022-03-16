from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.contrib.auth.models import User
from staff import models as CMODEL
from staff import forms as CFORM

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'vehicle/index.html')

def is_staff(user):
    return user.groups.filter(name='STAFF').exists()

def afterlogin_view(request):
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
        'total_vehicles':models.Vehicle.objects.all().count(),
        'total_vehicle_holders':models.VehicleRecord.objects.all().count(),
        'total_staff':CMODEL.Staff.objects.all().count(),
        'approved_vehicle_holders':models.VehicleRecord.objects.all().filter(status='Approved').count(),
        'disapproved_vehicle_holders':models.VehicleRecord.objects.all().filter(status='Disapproved').count(),
        'pending_vehicle_holders':models.VehicleRecord.objects.all().filter(status='Pending').count(),

    }
    return render(request, 'vehicle/admin_dashboard.html', context=dict)

@login_required(login_url='adminlogin')
def admin_view_staff_view(request):
    staffs=CMODEL.Staff.objects.all()
    return render(request, 'vehicle/admin-view-staff.html', {'staffs':staffs})


@login_required(login_url='adminlogin')
def update_staffs_view(request):
    staffs=CMODEL.Staff.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=staff.user_id)
    userForm=CFORM.StaffUserForm(instance=user)
    staffForm=CFORM.StaffForm(request.Files, instance=staff)
    mydict={'userForm':userForm, 'staffForm':staffForm}
    if request.method=='POST':
        userForm=CFORM.StaffUserForm(request.POST, instance=user)
        staffForm=CFORM.StaffForm(request.POST, request.FILES, instance=staff)
        if userForm.is_valid() and staffForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            staffForm.save()
            return HttpResponseRedirect('adminlogin')
    return render(request, 'vehicle/admin_update_staffs.html', context=mydict)



@login_required(login_url='adminlogin')
def delete_staffs_view(request, pk):
    staff=CMODEL.Staff.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=staff.user_id)
    user.delete()
    staff.delete()
    return HttpResponseRedirect('/admin-view-staffs')

def admin_add_vehicle_view(request):
    vehicleForm=forms.VehicleForm()

    if request.method=='POST':
        vehicleForm=forms.VehicleForm(request.POST)
        if vehicleForm.is_valid():
            vehicle=vehicleForm.save()
            vehicle.save()
            return redirect ('admin-view-vehicles')
    return render(request, 'vehicle/admin_add_vehicle.html', {'vehicleForm':vehicleForm})

def admin_view_vehicles_view(request):
    vehicles=models.Vehicle.objects.all()
    return render(request, 'vehicle/admin_view_vehicles.html', {'vehicles':vehicles})

def admin_update_vehicle_view(request):
    vehicles=models.Vehicle.objects.all()
    return render(request, 'vehicle/admin_update_vehicle.html', {'vehicles':vehicles})

@login_required(login_url='adminlogin')
def update_vehicle_view(request):
    vehicles=models.Vehicle.objects.get(id=pk)
    vehicleForm=forms.VehicleForm(instance=vehicle)

    if request.method=='POST':
        vehicleForm=forms.VehicleForm(request.POST, instance=vehicle)
        if vehicleForm.is_valid():
            vehicle=vehicleForm.save()
            vehicle.save()
            return redirect ('admin-view-vehicles')
    return render(request, 'vehicle/admin_update_vehicle.html', {'vehicles':vehicles})

def admin_delete_view(request):
    vehicles =models.Vehicle.objects.all()
    return render(request, 'vehicle/admin_delete_vehicle.html', {'vehicles':vehicles})

def delete_vehicle_view(request, pk):
    vehicle=models.Vehicle.objects.get(id=pk)
    vehicle.delete()
    return redirect('admin-view-vehicles')

def admin_view_vehicle_holder_view(request):
    vehiclerecords=models.VehicleRecord.objects.all()
    return render(request, 'vehicle/admin_view_vehicle_holder.html', {'vehicle_holders':vehicle_holders})

def admin_view_approved_vehicle_holder(request):
    vehiclerecords=models.VehicleRecord.objects.all().filter(status='Approved')
    return render(request, 'vehicle/admin_view_approved_vehicle_holder.html', {'vehicle_holders':vehicle_holders})

def admin_view_diasspproved_vehicle_holder(request):
    vehiclerecords=models.VehicleRecord.objects.all().filter(status='Disapproved')
    return render(request, 'vehicle/admin_view_disapproved_vehicle_holder.html', {'vehicle_holders':vehicle_holders})

def admin_view_waiting_vehicle_holder(request):
    vehiclerecords=models.VehicleRecord.objects.all().filter(status='Pending')
    return render(request, 'vehicle/admin_view_waiting_vehicle_holder.html', {'vehicle_holders':vehicle_holders})

def approve_request_view(request, pk):
    vehiclerecords = models.VehicleRecord.objects.get(id=pk)
    vehiclerecords.status='Approved'
    vehiclerecords.save()
    return redirect('admin-view-vehicle-holder')

def disapprove_request_view(request, pk):
    vehiclerecords = models.VehicleRecord.objects.get(id=pk)
    vehiclerecords.status='Disapproved'
    vehiclerecords.save()
    return redirect('admin-view-vehicle-holder')

