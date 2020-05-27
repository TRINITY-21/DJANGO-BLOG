from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']


#model forms create form working with a specific db

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta: 
        model = Profile
        fields = ['image']


