from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'condition']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter name"}),
        }