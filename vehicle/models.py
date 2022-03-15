from django.db import models
from django.contrib.auth.models import User
from staff.models import Staff

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=50)
    vehicle_holder = models.ForeignKey(Staff, on_delete=models.CASCADE)
    vehicle_status = models.BooleanField(default=False)
    vehicle_image = models.ImageField(upload_to='vehicle_images', blank=True)
    vehicle_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_type

class VehicleRecord(models.Model):
    vehicle_record_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_holder = models.ForeignKey(Staff, on_delete=models.CASCADE)
    vehicle_status = models.BooleanField(default=False)
    vehicle_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_record_id