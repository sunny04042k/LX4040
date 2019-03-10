from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserChangeForm
class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Firstname',max_length=30)
    last_name = forms.CharField(label='Lastname',max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password',widget=forms.PasswordInput)
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Invalid password")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Account name with special characters")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Account already exists")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'],first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'])

class EditProfileForm(UserChangeForm):
    class meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password'
        ]
