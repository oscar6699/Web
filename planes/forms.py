from django import forms
from .models import Plan_Contratado
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']