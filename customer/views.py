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



def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'customer/customerclick.html')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm, 'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_Customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_Customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'customer/customersignup.html', context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


@login_required(login_url='customerlogin')
def customer_dashboard_view(request):
    dict= {
        
        'customer':models.Customer.objects.get(user=request.user),
        'available_vehicles':CMODEL.Vehicle.objects.all().count(),
        'requested_vehicles':CMODEL.VehicleRecord.objects.all().count(),
    }
 
    return render(request, 'customer/customerdashboard.html', context=dict)

def request_vehicle_view(request):
    customer = models.Customer.objects.get(user=request.user)
    vehicles = CMODEL.Vehicle.objects.all()

    return render(request, 'customer/request_vehicle.html', {'customer': customer, 'vehicles': vehicles})

def requested_vehicles_view(request):
    customer = models.customer.objects.get(user_id=request.user.id)
    vehicles = CMODEL.Vehicles.objects.get(id=pk)
    vehiclerecords = CMODEL.VehicleRecord()
    vehiclerecords.vehicle = vehicle
    vehiclerecords.customer = customer
    vehiclerecords.save()
    return redirect('history')

def history_view(request):
    customer = models.Customer.objects.get(user=request.user)
    vehicle = CMODEL.VehicleRecord.objects.all().filter(customer=customer)
    return render(request, 'customer/history.html', {'customer': customer, 'vehicles': vehicles})