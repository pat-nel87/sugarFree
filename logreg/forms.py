# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:13:02 2021

@author: Patrick
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # you can set extra validations here to prevent is_valid from succeeding f you don't want it to.
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        # let's say we wanted to make our data all caps, we could do that here!
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
# returns a user with cleaned email, first_name, last_name
# pretty sure I still need to deal with the password?

