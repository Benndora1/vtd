from django import forms
from django.contrib.auth.models import User
from . import models


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = '__all__'