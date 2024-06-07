from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput


# - Register/Create a user
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=EmailInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
