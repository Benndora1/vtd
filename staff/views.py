from django.shortcuts import render,redirect,reverse
from . import forms, models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def staffclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'staff/staffclick.html')


def staffsignup_view(request):
    userForm=forms.StaffUserForm()
    staffForm=forms.StaffForm()
    mydict={'userForm':userForm, 'staffForm':staffForm}
    if request.method=='POST':
        userForm=forms.StaffUserForm(request.POST)
        staffForm=forms.StaffForm(request.POST)
        if userForm.is_valid() and staffForm.is_valid():
            user=userForm.save()
            staff=staffForm.save(commit=False)
            staff.user=user
            staff.save()
            my_staff_group=Group.objects.get_or_create(name='staff')
            my_staff_group[0].user_set.add(user)
        return HttpResponseRedirect('stafflogin')
    return render(request, 'staff/staffsignup.html', context=mydict)

def is_staff(user):
    return user.groups.filter(name='STAFF').exists()


@login_required(login_url='stafflogin')
def staff_dashboard_view(request):
    dict= {
        'staff':model.staff.objects.get(user=request.user)
    }
 
    return render(request, 'staff/dashboard.html', context=dict)

def request_vehicle_view(request):
    staff = models.Staff.objects.get(user_id=request.user.id)
    vehicles = CMODEL.vehicles.objects.all()
    return render(request, 'staff/request_vehicle.html', {'staff': staff, 'vehicles': vehicles})