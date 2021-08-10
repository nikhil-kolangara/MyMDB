from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserAuthentication

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text="First Name")
    last_name = forms.CharField(max_length=100, help_text="Last Name")
    email = forms.EmailField(unique=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
