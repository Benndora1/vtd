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