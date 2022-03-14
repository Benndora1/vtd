from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class StaffUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields= ['first_name', 'last_name', 'username', 'password']
         widgets = {
        'password': forms.PasswordInput()
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = ['address', 'mobile']
    