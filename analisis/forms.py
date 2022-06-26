
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AnalistaForm(ModelForm):
    class Meta:
        model = Analista
        fields = ['name', 'lastname', 'email', 'profile_pic']
        exclude = ['user']