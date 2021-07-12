from django import forms
from django.forms import fields
from .models import Lead

class CreateLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'name',
            'age',
            'phone_number',
            'agent'
        ]

