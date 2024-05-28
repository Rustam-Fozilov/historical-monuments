from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label='Email Address')
    password = forms.CharField(label='Password', max_length=100)

