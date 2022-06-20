from django import forms
from .models import customer
from django.forms import ModelForm, TextInput, EmailInput


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'Email'
                })
        }