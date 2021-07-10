from django import forms
from .models import Agent

class createAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'username',
            'age',
            'email',
        ]
