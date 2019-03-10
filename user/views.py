from django.shortcuts import render
from .forms import RegistrationForm, EditProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
import time
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/login')
    return render(request, 'REGISTER/index.html',{'form':form})
def profile_edit(request):
        if request.method ==   'POST':
                form = EditProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/user/profile')
        else:
                form = EditProfileForm(instance=request.user)
                args = {'form':form}
                return render(request,'USER_CHANGE/index.html',args)
def change_password(request):
        if request.method =='POST':
                form = PasswordChangeForm(request.POST,instance=request.user)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/user/profile/edit')
        else:
                form = PasswordChangeForm(request.POST,instace=request.user)
                args= {'form':form}
                return render(request,'USER_CHANGE/change_password.html',args)                
