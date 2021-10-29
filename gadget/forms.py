from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput, Select, FileInput
from gadget.models import SmartphoneDetail, SmartwatchDetail, LaptopDetail




class SmartphoneDetailForm(forms.ModelForm):
    class Meta:
        model = SmartphoneDetail
        fields = ['review', 'ratings']

class SmartwatchDetailForm(forms.ModelForm):
    class Meta:
        model = SmartphoneDetail
        fields = ['review', 'ratings']

class LaptopDetailForm(forms.ModelForm):
    class Meta:
        model = LaptopDetail
        fields = ['review', 'ratings']        
