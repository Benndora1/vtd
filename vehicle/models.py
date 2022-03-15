from django.db import models
from django.contrib.auth.models import User
from staff.models import Staff

STATUS = (
        ('Approved', "Approved"),
        ('Disapproved', "Disapprove"),
        ('Pending', "Pending"),
)
class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=50)
    vehicle_holder = models.ForeignKey(Staff, on_delete=models.CASCADE)
    vehicle_image = models.ImageField(upload_to='vehicle_images', blank=True)
    vehicle_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_type

class VehicleRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_holder = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=STATUS, default='Pending')
    vehicle_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vehicle

