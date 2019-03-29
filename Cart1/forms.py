from django.forms import ModelForm
from .models import Rentdays
from django import forms

class RentdaysForm(ModelForm):
    class Meta:
        model = Rentdays
        fields = ['days']