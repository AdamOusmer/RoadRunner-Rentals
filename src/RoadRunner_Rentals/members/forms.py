from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, help_text='')
    last_name = forms.CharField(max_length=100, help_text='')
    license = forms.CharField(max_length=100, help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile.objects.create(user=user, user_license=self.cleaned_data['license'])
        profile.save()

        return user
