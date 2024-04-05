# forms.py
from django import forms
from .models import QuickFormData
from .models import Registration


class QuickForm(forms.ModelForm):
    class Meta:
        model = QuickFormData
        fields = ['assignee_email', 'title', 'description']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'contact', 'gender', 'password']

