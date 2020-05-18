from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from core.models import Profile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'email', 'bio',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']