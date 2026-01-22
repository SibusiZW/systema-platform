from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput({'class': 'input', 'placeholder': 'Enter password'}))