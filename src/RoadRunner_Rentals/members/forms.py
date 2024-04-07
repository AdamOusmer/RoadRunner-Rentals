from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, help_text='')
    last_name = forms.CharField(max_length=100, help_text='')
    license = forms.CharField(max_length=100, help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'license', 'password1', 'password2']
